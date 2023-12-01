#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parm"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    res = requests.post(url, data=value)
    print(res.text)
