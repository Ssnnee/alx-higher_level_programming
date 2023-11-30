#!/bin/bash
# Gives the size of the body of the response of a given URL
curl -sI "$1" | grep -i Content-length | awk '{print $2}'
