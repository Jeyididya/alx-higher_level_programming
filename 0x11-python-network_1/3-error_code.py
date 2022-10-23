#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body.
"""


if __name__ == "__main__":
    import sys
    from urlib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('ERROR code:', er.code)
