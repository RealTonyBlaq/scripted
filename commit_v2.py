#!/usr/bin/env python3
""" Script manages Git commands - add, commit and push """

import git
import git.repo
import redis
from sys import argv
import os


file = None
try:
    file = argv[1]
except IndexError:
    pass

redis_client = redis.Redis()


if not file:
    cwd = os.getcwd()
    try:
        repo = git.Repo(cwd)
    ex

    print(repo.untracked_files)
    print([file.a_path for file in repo.index.diff(None)])
