#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    git_username = sys.argv[1]
    git_password = sys.argv[2]
    req_url = "https://api.github.com/user"
    credentials = requests.get(req_url, auth=(git_username, git_password))
    try:
        print(credentials.json()["id"])
    except KeyError:
        print("None")
