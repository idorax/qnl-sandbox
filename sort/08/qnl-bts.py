#!/usr/bin/python3

import sys
import math
#import pysnooper


class InputError(Exception):
    pass


def detect_type_of_element(array):
    """
    Detect the type of per element in array.

    :param array: String array whose element may be ``integer`` or ``char``, e.g.
                  ['1', '2', '3'] # The type of per element is ``int``
                  ['a', 'b', 'c'] # The type of per element is ``str``

    :returns: int or str
    """

    target_types = []
    for element in array:
        try:
            _ = int(element)
            element_type = int
        except: element_type = str
        target_types.append(element_type)

    if len(set(target_types)) > 1:
        raise InputError("The type of per element in the array is not of the same one!")

    return target_types[0]


def args2array(args):
    """
    Convert args to array.

    :param args: a list of args and the type of each element is str.

    :returns: A tuple of array and element type.
    """

    element_type = detect_type_of_element(args)
    if element_type is int:
        array = [int(e) for e in args]
    elif element_type is str:
        array = [ord(e[0]) for e in args]
    return (array, element_type)


def show_array(prefix, element_type, array):
    """
    Show array to user.

    :param prefix: The prefix of message to show.
    :param element_type: The type of element, str or int.
    :param array: A list of integers.

    :returns: None.
    """

    if element_type is str:
        out_list = [chr(e) for e in array]
    else:
        out_list = [str(e) for e in array]
    print(f"{prefix}: {', '.join(out_list)}")


#@pysnooper.snoop(prefix='DEBUG:get_width_of_num()> ')
def get_width_of_num(n):
    """
      0,   1, ...,   9: 1
     10,  11, ...,  99: 2
    100, 101, ..., 999: 3
    """
    if n == 0:
        return 1
    return math.floor(math.log(n, 10)) + 1


#@pysnooper.snoop(prefix='DEBUG:get_hash_base()> ')
def get_hash_base(a):
    max_num = max(a)

    base = 1
    for i in range(get_width_of_num(max_num)):
        base *= 10
    return base


#@pysnooper.snoop(prefix='DEBUG:scatter()> ')
def scatter(buckets, buckets_num, a, n):
    hash_base = get_hash_base(a) 
    for i in range(n):
        bucket_id = a[i] * buckets_num // hash_base
        buckets[bucket_id].append(a[i])


#@pysnooper.snoop(prefix='DEBUG:gather()> ')
def gather(buckets, buckets_num, a, n):
    k = 0
    for i in range(buckets_num):
        if not buckets[i]:
            continue

        # copy buckets[i] to a[]
        a[k:] = buckets[i][:]
        k += len(buckets[i])

        # Error: overflow
        if k >= n:
            break


#@pysnooper.snoop(prefix='DEBUG:walk_and_sort()> ')
def walk_and_sort(buckets, buckets_num):
    for i in range(buckets_num):
        if buckets[i]:
            buckets[i].sort()


# The total number of our buckets
BUCKETS_NUM = 10


#@pysnooper.snoop(prefix='DEBUG:bucketsort()> ')
def bucketsort(a):
    n = len(a)

    # allocate buckets[]
    buckets = []
    for i in range(BUCKETS_NUM):
        buckets.append([])

    # scatter elements in a[] to buckets[]
    scatter(buckets, BUCKETS_NUM, a, n)

    # walk buckets[] and sort
    walk_and_sort(buckets, BUCKETS_NUM)

    # gather all elements from buckets[] and save them into a[]
    gather(buckets, BUCKETS_NUM, a, n)


def main(argc, argv):
    if argc < 2:
        print(f"Usage: {argv[0]} <N1> [N2] ...", file=sys.stderr)
        return 1

    array, element_type = args2array(argv[1:])
    show_array("Before sorting", element_type, array)
    bucketsort(array)
    show_array("After  sorting", element_type, array)

    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
