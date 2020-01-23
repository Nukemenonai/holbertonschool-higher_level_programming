#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """ Rectangle class, inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ inits an instance of the rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, width):
        """ """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, height):
        """ """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """ """
        return self.__x

    @x.setter
    def x(self, x):
        """ """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ """
        return self.__y

    @y.setter
    def y(self, y):
        """ """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
