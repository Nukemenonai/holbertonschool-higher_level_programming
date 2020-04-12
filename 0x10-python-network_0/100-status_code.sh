#!/bin/bash
# this script returs status code only
curl -sw "%{http_code}" "$1" -X HEAD
