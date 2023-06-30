#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url_req = requests.get('https://alx-intranet.hbtn.io/status')
    status_text = url_req.text
    print('Body response:')
    print('\t- type: {}'.format(type(status_text)))
    print('\t- content: {}'.format(status_text))
