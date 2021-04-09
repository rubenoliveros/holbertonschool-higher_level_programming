#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as rq:
        print("Body response:")
        print("\t- type: {}".format(type(rq.peek())))
        print("\t- content: {}".format(rq.peek()))
        print("\t- utf8 content: {}".format(rq.peek().decode('utf-8')))
