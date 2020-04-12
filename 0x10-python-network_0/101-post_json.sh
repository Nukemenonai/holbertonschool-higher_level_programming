#!/bin/bash
# this script returs status code only
curl -X POST -k -i -H "Accept: application/json" -H "Content-Type: application/json" -w "%{body}" -w "%{http_code}" -d "$2" "$1"
