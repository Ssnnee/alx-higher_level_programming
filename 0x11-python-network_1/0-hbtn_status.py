#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request


header = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(
        'https://intranet.hbtn.io/status', headers=header
)

with urllib.request.urlopen(req) as response:
    res = response.read()
    print("Body response:")
    print("\t- type: {}".format(res.__class__))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode('ascii')))
