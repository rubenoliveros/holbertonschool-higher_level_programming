#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server accepts
curl -sI localhost:5000/route_4 | grep "Allow" | cut -d' ' -f2-  
