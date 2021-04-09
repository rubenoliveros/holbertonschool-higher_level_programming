#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
# The size must be displayed in bytes
# You have to use curl

curl -Is "$1" | grep 'Content-Length' | awk 'NF>1{print $NF}'
