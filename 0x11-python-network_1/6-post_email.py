#!/usr/bin/python3

"""this script fetches"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post("{}".format(sys.argv[1]),
                      data={'email': "{}".format(sys.argv[2])})
    print(r.text)
