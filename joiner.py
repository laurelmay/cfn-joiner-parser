#!/usr/bin/env python3

import sys
import yaml


def main():
    args = sys.argv[1:]
    file = args[0] if args else sys.stdin

    chars = list(file.read())
    join = {'Fn::Join': ['', chars]}
    yaml.safe_dump(join, sys.stdout, default_flow_style=False)


if __name__ == '__main__':
    sys.exit(main())
