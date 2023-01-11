#!/usr/bin/python3
"""Defines class Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with width"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return description of the square"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Return area of the square"""
        return self.__size ** 2
