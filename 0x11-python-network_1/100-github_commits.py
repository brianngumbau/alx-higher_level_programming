#!/usr/bin/python3
"""takes 2 arguments in order to solve given challenge
(lists 10 commits of the repository "rails" by user "rails"
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
