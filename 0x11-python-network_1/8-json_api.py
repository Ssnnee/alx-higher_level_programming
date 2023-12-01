#!/usr/bin/python3
"""POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    parm = {'q': letter}

    try:
        res = requests.post(url, data=parm)

        try:
            json = res.json()
            if json:
                print("[{}] {}".format(json['id'], json['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print("Error: {}".format(e))
