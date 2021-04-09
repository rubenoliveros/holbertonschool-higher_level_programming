#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
curl -Is "$1" | grep 'Content-Length' | awk 'NF>1{print $NF}'
