#!/usr/bin/env python3
""" Script manages Git commands - add, commit and push. """

from datetime import datetime
import git
from git.exc import InvalidGitRepositoryError
import os
import redis
from sys import argv
import signal
import time


file = None
cwd = os.getcwd()
redis_client = redis.Redis()
push_count = 0
date_format = "%Y-%m-%d"
today = datetime.now().strftime(date_format)

try:
    file = argv[1]
except IndexError:
    pass

try:
    repo = git.Repo(cwd)
except InvalidGitRepositoryError as e:
    dir = e.args[0].split('/')[3]
    repo = git.Repo(f'/home/tony/{dir}')


new_files = repo.untracked_files
changed_files = [file.a_path for file in repo.index.diff(None)]

# SIGINT handler
def handler(signum=None, frame=None):
    """ Executed when CTRL+C is called """
    # Retrieve previous commit count from Redis
    key = f'day_{today}'
    commit_count = redis_client.get(key) or 0
    today_commit = commit_count + push_count

    # Update commit count
    redis_client.set(key, )
    print(f'\nYou contributed to Open Source {today_commit} times today - {date_format}')
    print("Process terminated..")
    exit(0)

signal.signal(signal.SIGINT, handler)


# Commit function
def push_to_repo(files: list) -> int:
    """ Commits to the repository """
    count = 1
    print('\nCommitted files:')
    for file in files:
        message = input(f'Please enter a commit message for {file}: ')
        repo.git.add(file)
        repo.git.commit('-m', message)
        repo.git.push()

        print(f'\t {count}. {file}')
        count += 1
        time.sleep(2)

    return len(files)


if not file:

    push_count = push_to_repo(changed_files)

    if len(new_files) != 0:
        print(f'There are {len(new_files)} untracked files => {new_files}')
        reply = input('Do you want to push them [Y/N]? ').lower()
        if reply in ['y', 'yes']:
            push_count += push_to_repo(new_files)

else:
    message = input(f'Please enter a one-time commit message for {file}: ')
    while True:
        if file not in changed_files:
            time.sleep(120)
            continue
        repo.git.add(file)
        repo.git.commit('-m', message)
        repo.git.push()

        push_count += 1

        time.sleep(300)


handler()
