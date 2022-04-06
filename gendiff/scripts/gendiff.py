#!/usr/bin/env python3
import argparse
from gendiff.gendiff import generate_diff
# from gendiff.formatters import stylish


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        # choices=[]
        help='set format of output (default: stylish)'
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
