#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import urllib.request as req_fetch
from sys import argv
if __name__ == "__main__":
    with req_fetch.urlopen(req_fetch.Request(argv[1])) as req_url:
        print(req_url.headers.get('X-Request-Id'))
