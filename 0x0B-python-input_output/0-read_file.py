#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """""reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
