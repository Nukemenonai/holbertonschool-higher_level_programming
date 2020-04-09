#!/bin/bash
# this script gets the size in bytes of the body of a response.
curl -s "$1" | wc -c
