#!/bin/bash
# this script uploads JSON
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
