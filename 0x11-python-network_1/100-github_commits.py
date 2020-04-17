#!/usr/bin/python3

"""this script fetches something """

import requests
import sys


if __name__ == "__main__":

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[1],
                             sys.argv[2]))
    data = r.json()
    for i in range(10):
        print("{}: {}".format(data[i].get('sha'),
                              data[i].get('commit').get('author').get('name')))
