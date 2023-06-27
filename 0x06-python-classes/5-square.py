#!/usr/bin/python3
""" Square class def"""


class Square:
    """attributes"""
    def __init__(self, size=0):
        """ size init"""
        self.size = size

    def area(self):
        """ returns the size squared"""
        return self.__size ** 2

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#"for j in range(self.size)]))
