#!/usr/bin/python3
"""Sends request to URL and displays the value of the X-request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
