#!/usr/bin/python3
"""wrtie_file"""


def write_file(filename="", text=""):
    """returns the number of characters written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
