#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ instantiates a rectangle """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        "string representation of a rectangle"
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """ represents a rectangle """
        return "[Rectangle]{}/{}".format(self.__width, self.__height)

    def area(self):
        """ area """
        return self.__width * self.__height
