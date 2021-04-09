#!/bin/bash
# A Bash script that takes in a URL and displays the size of the body
curl -Is "$1" | grep 'Content-Length' | awk 'NF>1{print $NF}'
