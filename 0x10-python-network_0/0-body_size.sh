#!/bin/bash
# this script gets the size in bytes of the body of a response.
curl -s 0.0.0.0:5000 | wc -c
