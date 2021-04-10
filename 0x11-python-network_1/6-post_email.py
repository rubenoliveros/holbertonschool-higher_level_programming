#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    email = {'email': argv[2]}
    p = requests.post(argv[1], email)
    print(p.text)
