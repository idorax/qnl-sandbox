#!/usr/bin/python3
"""
Encode or decode a text file with password. Note that base64 is used.
For more about it, please refer to:
    https://blog.csdn.net/weixin_44799217/article/details/125949538
"""

import sys
import argparse
import base64


__version__ = '1.0.0'


def _raw_encode(s):
    s_encode = s.encode(encoding='utf-8')
    s_base64 = base64.b64encode(s_encode)
    return s_base64.decode(encoding='utf-8')


def _raw_decode(s):
    s_encode = s.encode(encoding='utf-8')
    s_base64 = base64.b64decode(s_encode)
    return s_base64.decode(encoding='utf-8')


def encode(s):
    sp = _raw_encode(s)
    return _raw_encode(sp.swapcase())


def decode(s):
    sp = _raw_decode(s)
    return _raw_decode(sp.swapcase())


def encode_with_passwd(s, passwd):
    password = encode(passwd)
    head = f"<{password}>"
    tail = f"</{password}>"
    text = f"{head}{s}{tail}"
    return encode(text)


def decode_with_passwd(s, passwd):
    password = encode(passwd)
    head = f"<{password}>"
    tail = f"</{password}>"
    text = decode(s)
    if text.startswith(head) and text.endswith(tail):
        return text.lstrip(head).rstrip(tail)
    return 'Oops\n'


def load_yaml_file(yaml_file):
    text = ''
    with open(yaml_file, 'r') as file_handler:
        text = ''.join(file_handler.readlines())
    return text


def main(argc, argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encode', action='store_true', default=False, help='encode plain text')
    parser.add_argument('-d', '--decode', action='store_true', default=False, help='decode base64 text')
    parser.add_argument('-t', '--test',  action='store_true', default=False, help='test')
    parser.add_argument('-f', '--file', required=True, type=str, help='plain or base64 text file')
    parser.add_argument('-p', '--password',  type=str, default='0x41', help='password')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    args = parser.parse_args()

    text = load_yaml_file(args.file)

    if args.test:
        s0 = encode_with_passwd(text, args.password)
        s1 = decode_with_passwd(s0, args.password)
        if args.verbose:
            print(f">>> In:  [{text}]")
            print(f">>> B64: [{s0}]")
            print(f">>> Out: [{s1}]")

        if s1 == text:
            print("PASS")
            return 0
        else:
            print("FAIL")
            return 1
    elif args.encode:
        print(encode_with_passwd(text, args.password), end='\n')
        return 0
    elif args.decode:
        print(decode_with_passwd(text, args.password), end='')
        return 0
    else:
        print("UNSUPPORTED", file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
