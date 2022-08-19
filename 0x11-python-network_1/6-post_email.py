#!/usr/bin/python3
"""Send a POST request to the passed url display the body of the response"""
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    myobj = {'email': sys.argv[2]}

    req = requests.post(url, myobj)
    print(req.text)
