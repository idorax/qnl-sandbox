#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Public functions to print out colorful string on terminal
"""

import sys
import os


def isatty():
    s = os.getenv("ISATTY")
    if s is None:
        s = ""
    if s.upper() == "YES":
        return True
    if s.upper() == "NO":
        return False
    if sys.stdout.isatty() and sys.stderr.isatty():
        return True
    return False


def str2gray(s):
    return f"\033[1;30m{s}\033[m" if isatty() else s


def str2red(s):
    return f"\033[1;31m{s}\033[m" if isatty() else s


def str2green(s):
    return f"\033[1;32m{s}\033[m" if isatty() else s


def str2yellow(s):
    return f"\033[1;33m{s}\033[m" if isatty() else s


def str2blue(s):
    return f"\033[1;34m{s}\033[m" if isatty() else s


def str2magenta(s):
    return f"\033[1;35m{s}\033[m" if isatty() else s


def str2cyan(s):
    return f"\033[1;36m{s}\033[m" if isatty() else s


def str2white(s):
    return f"\033[1;37m{s}\033[m" if isatty() else s


def main(argc, argv):
    s = ' '.join(argv[1:]) if argc >= 2 else "Hello World!"
    print(str2gray(s))
    print(str2red(s))
    print(str2green(s))
    print(str2yellow(s))
    print(str2blue(s))
    print(str2magenta(s))
    print(str2cyan(s))
    print(str2white(s))
    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
