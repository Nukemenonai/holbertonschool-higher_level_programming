#!/usr/bin/python3

"""this script fetches something """

import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.post("http://0.0.0.0:5000/search_user",
                          data={'q': "{}".format((sys.argv[1]
                                                 if (len(sys.argv) == 2)
                                                 else ""))})
        if r.json().get('id') is not None:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
