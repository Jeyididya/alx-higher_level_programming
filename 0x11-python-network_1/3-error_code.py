#!/usr/bin/python3
""" error code """
import urllib.request
import sys


if __name__ == "__main__":
<<<<<<< HEAD
    import sys
    from urllib import request, error

=======
    req = urllib.request.Request(sys.argv[1])
>>>>>>> c4957ecd3342f25eac7b230d22761c0460ca3c45
    try:
        urllib.request.urlopen(req)
        with urllib.request.urlopen(req) as res:
            bc = res.read().decode('utf-8')
            print(bc)
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
