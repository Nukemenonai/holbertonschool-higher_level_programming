#!/bin/bash
# this script gets the size in bytes of the body of a response.
curl -sI X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
