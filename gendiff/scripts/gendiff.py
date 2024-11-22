#!/usr/bin/env python

from gendiff.cli import parse
from gendiff.diff_with_formatter import generate_diff


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file, formater=args.format)
    print(diff)


if __name__ == '__main__':
    main()
