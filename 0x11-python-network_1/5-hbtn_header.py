#!/usr/bin/python3

"""this script fetches"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get("{}".format(sys.argv[1]))
    print(r.headers.get('X-Request-Id'))
