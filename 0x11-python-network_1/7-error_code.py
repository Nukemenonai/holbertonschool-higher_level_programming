#!/usr/bin/python3

"""this script fetches something """

import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get("{}".format(sys.argv[1]))
        r.raise_for_status()
        print(r.text)
    except HTTPError:
        print("Error code: {}".format(r.status_code))
