#!/usr/bin/env python3

import sys
import yaml


def main():
    args = sys.argv[1:]
    file = args[0] if args else sys.stdin

    data = yaml.safe_load(file)
    join_args = data['Fn::Join']
    contents = join_args[0].join(join_args[1])
    print(contents, end='')


if __name__ == '__main__':
    sys.exit(main())
