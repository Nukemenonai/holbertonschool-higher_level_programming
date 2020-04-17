#!/usr/bin/python3

"""this script fetches something """

import requests
import sys
import base64


if __name__ == "__main__":
    client_key = sys.argv[1]
    client_secret = sys.argv[2]

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')

    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': "{}".format(sys.argv[3]),
        'count': 5
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url,
                               headers=search_headers, params=search_params)

    Data = search_resp.json().get("statuses")
    for r in Data:
        print("[{}] {} by {}".format(r['id'], r['text'], r['user']['name']))
