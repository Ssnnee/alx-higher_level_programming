#!/bin/bash
# Send a JSON POST request and display the body of the response
curl -sX POST -d @"$2" -H "Content-Type: application/json"  "$1"
