#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""
if __name__ == "__main__":
    import urllib.parse as par
    import urllib.request as req
    from sys import argv
    email = {'email': argv[2]}
    email_address = par.urlencode(email).encode('utf-8')
    rq = req.Request(argv[1], email_address)
    with req.urlopen(rq) as page:
        print(page.read().decode('utf-8'))
