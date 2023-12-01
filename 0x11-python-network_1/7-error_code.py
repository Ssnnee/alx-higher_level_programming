#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(res.status_code))
