#!/bin/bash
# A script that takes in a URL as argument, and displays the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
