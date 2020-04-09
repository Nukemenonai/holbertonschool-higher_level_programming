#!/bin/bash
# this script gets the size in bytes of the body of a response.
curl -siX "$1" | grep Allow: | cut -d' ' -f2-
