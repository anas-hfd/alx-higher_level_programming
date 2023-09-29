#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        content = data.decode(UTF-8)
        print ("Body response:")
        print ("\t- type: {}".format(type(data)))
        print ("\t- content: {}".format(data))
        print ("\t- utf-8 content: {}".format(content))
