#!/bin/bash
# this script returs status code only
curl -sL -X POST -H "Content-Type: application/json" -d "$2" "$1"
