#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request as req_fetch
if __name__ == "__main__":
    with req_fetch.urlopen('https://alx-intranet.hbtn.io/status') as req_url:
        html = req_url.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
