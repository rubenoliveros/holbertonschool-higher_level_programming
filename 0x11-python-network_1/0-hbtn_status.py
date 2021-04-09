#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request as req
    with req.urlopen('https://intranet.hbtn.io/status') as rq:
        status = rq.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(status.decode('utf-8')))
