#!/usr/bin/python3
"""log parsing"""

import fileinput
import sys
import os

i = size = 0
dict = {'200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0}

try:
    for line in sys.stdin:
        i += 1
        size += int(line.split()[-1])
        dict[str(line.split()[7])] += 1
        if i % 10 == 0:
            print("File size: {}".format(size))
            for key in sorted(dict.keys()):
                if dict[key] != 0:
                    print("{}: {}".format(key, dict[key]))
except KeyboardInterrupt:
    print("File size: {}".format(size))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))
            dict[key] = 0
