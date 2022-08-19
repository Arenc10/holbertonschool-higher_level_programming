#!/usr/bin/python3
"""Sends a request to URL and displays the body of the response"""
import urllib
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


if __name__ == "__main__":

    url = sys.argv[1]
    req = Request(url)

    try:
        with urllib.request.urlopen(req) as reponse:
            print(response.read().decode("utf-8"))
    except URLError as e:
        print("Error code:", e.code)
