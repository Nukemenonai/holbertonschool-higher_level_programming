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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x,
                                                 self.__y, self.__size,)

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

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if args and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary representation of a square """
        return {'id': self.id, 'size':self.__size, 'x': self.__size,
                'y': self.__y}
