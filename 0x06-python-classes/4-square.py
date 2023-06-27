#!/usr/bin/python3
"""Square class definition """


class Square:
    """attributes"""
    def __init__(self, size=0):
        """initialiazation"""
        self.size = size

    def area(self):
        """returns the square area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size value"""
        if type(value) is not int:
            raise TypeError('size must be an intiger')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
