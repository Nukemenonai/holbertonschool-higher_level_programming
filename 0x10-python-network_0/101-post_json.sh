#!/bin/bash
# this script returs status code only
curl -X POST -H "Content-Type: application/json"  -d @"$2" "$1"
