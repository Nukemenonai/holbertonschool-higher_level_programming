#!/usr/bin/python3

"""this script fetches something """

import requests
import sys


if __name__ == "__main__":
    token = sys.argv[2]
    user = sys.argv[1]
    r = requests.get('https://api.github.com/users/' + user,
                     auth=(user, token))
    print(r.json().get('id'))
