#!/usr/bin/python3
"""
takes in URL & email, sends a POST request to the URL
with the email as a parameter, and finally displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}

    req = requests.post(url, data=mail)
    print(req.text)
