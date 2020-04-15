#!/usr/bin/python3

"""this script fetches an URL """

from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({'email': "{}".format(sys.argv[2])}).encode()
    req = request.Request("{}".format(sys.argv[1]), data=data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('UTF-8'))
