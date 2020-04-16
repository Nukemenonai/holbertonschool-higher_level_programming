#!/usr/bin/python3
"""this script fetches an URL """

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as resp:
        print(resp.getheader('X-Request-Id'))
