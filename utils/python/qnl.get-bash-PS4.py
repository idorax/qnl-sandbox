#!/usr/bin/python3
"""
#!/bin/bash

function _initPS4
{
    export PS4='[${FUNCNAME}@${BASH_SOURCE}:${LINENO}|${SECONDS}]+ '
}

function DEBUG
{
    typeset -l s=$DEBUG
    [[ $s == "yes" || $s == "true" ]] && _initPS4 && set -x
}
"""

import sys


def main(argc, argv):
    print(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
