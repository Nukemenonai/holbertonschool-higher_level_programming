#!/usr/bin/python3

"""this script fetches an URL """

from urllib import request, parse
import urllib
import sys


if __name__ == "__main__":
        try:
                with request.urlopen("{}".format(sys.argv[1])) as resp:
                        print(resp.read().decode('UTF-8'))
        except urllib.error.HTTPError as e:
                print("Error code: {}".format(e.code))
