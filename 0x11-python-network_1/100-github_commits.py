#!/usr/bin/python3

"""this script fetches something """

import requests
import sys


if __name__ == "__main__":

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[1],
                             sys.argv[2]))
    data = r.json()
    for i in data[:10]:
        print("{}: {}".format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
