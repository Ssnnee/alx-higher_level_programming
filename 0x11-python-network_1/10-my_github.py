#!/usr/bin/python3
"""Display the github id using the github API"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
