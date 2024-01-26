#!/usr/bin/python3
"""Takes in a URL, send a request to URL, and dispaly body"""

import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
