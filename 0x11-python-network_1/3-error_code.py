#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request as url_request
import urllib.error as url_error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req_url = url_request.Request(url)
    try:
        with url_request.urlopen(req_url) as url_response:
            print(url_response.read().decode('utf-8'))
    except url_error.HTTPError as http_err:
        print("Error code: {}".format(http_err.code))
