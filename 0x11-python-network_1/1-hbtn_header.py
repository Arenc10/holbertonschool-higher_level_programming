#!/usr/bin/python3
"""Sends request to URL and displays the value of the X-request-Id"""
import urllib.request
import sys


url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
