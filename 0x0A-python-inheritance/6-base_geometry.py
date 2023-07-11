#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
