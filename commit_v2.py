#!/usr/bin/env python3
""" Script manages Git commands - add, commit and push """

import git
import redis
from sys import argv
import os


file = argv[1]
redis_client = redis.Redis()


if not file:
    cwd = os.getcwd()
    print(cwd)
