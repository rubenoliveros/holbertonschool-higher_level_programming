#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    user_pass = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                             auth=requests.auth.HTTPBasicAuth(argv[1],
                             argv[2]))
    print(user_pass.json().get('id'))
