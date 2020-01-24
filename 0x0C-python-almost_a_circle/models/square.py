#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class, inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ instatiates a square """
        self.__x = x
        self.__y = y
        self.__size = size
        super().__init__(self.__size, self.__size, self.__x, self.__y)

    def __str__(self):
        """ representas a square """
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                    self.__y, self.__size,
                                                    self.__size)

    @property
    def size(self):
        """ property size """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = size
