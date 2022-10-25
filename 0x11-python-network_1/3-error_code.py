#!/usr/bin/python3
""" error code """
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
        with urllib.request.urlopen(req) as res:
            bc = res.read().decode('utf-8')
            print(bc)
    except urllib.error.HTTPError as er:
        print('ERROR code:', er.code)
