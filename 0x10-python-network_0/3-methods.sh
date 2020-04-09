#!/bin/bash
# this script gets the size in bytes of the body of a response.
curl -I "$1" | grep Allow: | sed -e "s/Allow: //"
