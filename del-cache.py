#!/usr/bin/python3
"""
Script deletes all __pycache__ directories in a directory
and it's sub-directories
"""
import os
import shutil
import time
import sys


def deleteCache(cwd, directory):
    """
    Recursively deletes a directory in the given directory
    and its sub-directories.

    Args:
        cwd (str): The current working directory to search
                    for the file.
        directory (str): The name of the directory to delete.
    """
    for root, dirs, files in os.walk(cwd):
        for dir in dirs:
            if dir == '.venv':
                continue
            if dir == directory:
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path)
                continue
            deleteCache(os.path.join(root, dir), directory)


if __name__ == "__main__":
    # Starting an execution time counter
    start = time.perf_counter()
    cwd = os.getcwd()
    deleteCache(cwd, '__pycache__')
    # Execution time gotten
    end = time.perf_counter() - start
    print(f'Executed in {end:.2f}ms')
    sys.exit(0)
