#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server accepts
curl -sI "$1"/route_4 | grep "Allow" | sed 's/^Allow: //'    
