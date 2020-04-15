#!/usr/bin/python3
"""this script fetches an URL """

import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as resp:
        data = resp.read()
        html = data.decode("UTF-8")

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(html))
