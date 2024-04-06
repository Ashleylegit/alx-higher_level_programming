#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        fetched = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(fetched)))
        print("\t- content: {}".format(fetched))
        print("\t- utf8 content: {}".format(fetched.decode('utf-8')))
