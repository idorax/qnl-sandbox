#!/usr/bin/python3
"""
Get the total number of primes not exceeding N
"""

import sys


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    m = int(n ** 0.5) + 1
    for i in range(m + 1):
        if i == 0 or i == 1:
            continue
        if n % i == 0:
            return False
    return True



def get_num_of_primes(n):
    list_primes = []
    for i in range(n + 1):
        if i == 0:
            continue
        if is_prime(i):
            list_primes.append(i)
    #print(list_primes)
    num = len(list_primes)
    return num


def main(argc, argv):
    if argc != 2:
        print(f"Usage: {argv[0]} <N>", file=sys.stderr)
        print("e.g.")
        print(f"       {argv[0]} 1368", file=sys.stderr)
        print(f"       {argv[0]} 64", file=sys.stderr)
        print(f"       {argv[0]} $((1368 * 64))", file=sys.stderr)
        print(f"       {argv[0]} 100", file=sys.stderr)
        return 1

    n = int(argv[1])
    print(get_num_of_primes(n))
    return 0


if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
