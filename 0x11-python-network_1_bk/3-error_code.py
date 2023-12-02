#!/usr/bin/python3
"""
Sends a request to a URL & displays the body of the response.
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
