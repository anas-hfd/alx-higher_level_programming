#!/usr/bin/python3
"""Square class def"""


class Square:
    """Attributes"""
    def __init__(self, size=0):
        """square init"""
        self.size = size

    def area(self):
        """returns the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """less than"""
        return self.size < other.size

    def __le__(self, other):
        """ less than or equal"""
        return self.size <= other.size

    def __eq__(self, other):
        """equal sizes"""
        return self.size == other.size

    def __ne__(self, other):
        """not equal"""
        return self.size != other.size

    def __ge__(self, other):
        """greater or equal"""
        return self.size >= other.size

    def __gt__(self, other):
        """greater than"""
        return self.size > other.size
