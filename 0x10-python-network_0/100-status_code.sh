#!/bin/bash
# Sends request to a given URL and displays only the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
