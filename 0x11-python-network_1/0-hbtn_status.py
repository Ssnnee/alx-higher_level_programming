#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    res = response.read().decode('utf-8')

print(f"Body response:\n\t- type: {type(res)}\n\t- content: {res}\n\t- utf8 content: {res.decode('utf-8')}")
