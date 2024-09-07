#!/usr/bin/env python3
""" Script manages Git commands - add, commit and push """

import git
import redis
from sys import argv


file = argv[1]
redisclient = redis.Redis()
