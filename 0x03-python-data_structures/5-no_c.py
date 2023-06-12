#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            nstr += x
    return nstr
