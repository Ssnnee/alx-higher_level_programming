#!/bin/bash
# Show all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | awk -F ': ' '/Allow:/ {gsub(/ /, " ", $2); print $2}'
