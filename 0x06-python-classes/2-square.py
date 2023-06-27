#!/usr/bin/python3
"""Square class definition"""


class Square:
    """attributes"""
    def __init__(self, size=0):
        """"instantiation with size"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
