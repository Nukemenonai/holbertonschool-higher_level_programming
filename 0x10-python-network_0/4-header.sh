#!/bin/bash
# seds a get request and displays the body
curl -sH "X-HolbertonSchool-User-Id:98" "$1" -X GET
