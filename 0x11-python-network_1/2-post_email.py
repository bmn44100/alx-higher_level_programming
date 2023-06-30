#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request as url_request
import urllib.parse as parse_url
from sys import argv

if __name__ == "__main__":
    post_url = argv[1]
    url_data = {'email' : argv[2]}
    url_data = parse_url.urlencode(url_data)
    url_data = url_data.encode('ascii')
    req_url = url_request.Request(post_url, url_data)
    with url_request.urlopen(req_url) as response:
        print(response.read().decode('utf-8'))
