#!/bin/bash
# this script returs status code only
curl -sX POST -H "Content-Type: application/json" -d $(cat "$2") "$1"
