#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    post_url = 'http://0.0.0.0:5000/search_user'
    url_data = {'q': q}
    try:
        url_req = requests.post(post_url, data=url_data).json()
        if 'id' in url_req and 'name' in url_req:
            print("[{}] {}".format(url_req['id'], url_req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
