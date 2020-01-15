#!/usr/bin/python3
class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ init method for my class
       args:
           width:
           height:
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """property height for rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """ defines the heigh of the rectangle"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ width property of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """Init method for rectangle class
        Args:
        width: width of the rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """defines the area of my rectangle"""
        if self.__width == 0 or self.__height == 0:
            area = 0
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        """ defines the perimeter of my rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = (self.__width + self.__height) * 2
        return (perimeter)
