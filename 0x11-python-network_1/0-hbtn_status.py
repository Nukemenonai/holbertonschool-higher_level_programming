#!/usr/bin/python3
"""this script fetches an URL """

import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as resp:
        data = resp.read()
        html = data.decode("UTF-8")

        print("Body Response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(html))
