#!/bin/bash
# this script returs status code only
curl -sL -w "%{http_code}" 0.0.0.0:5000 -X HEAD
