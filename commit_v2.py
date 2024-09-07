#!/usr/bin/env python3
""" Script manages Git commands - add, commit and push """

import git
from git.exc import InvalidGitRepositoryError
import redis
from sys import argv
import os


file = None
try:
    file = argv[1]
except IndexError:
    pass

redis_client = redis.Redis()
redis_client.close()

if not file:
    cwd = os.getcwd()
    try:
        repo = git.Repo(cwd)
    except InvalidGitRepositoryError as e:
        dir = e.args[0].split('/')[3]
        repo = git.Repo(f'/home/tony/{dir}')

    new_files = repo.untracked_files
    changed_files = [file.a_path for file in repo.index.diff(None)]


    for file
    print(changed_files)
    repo.close()
