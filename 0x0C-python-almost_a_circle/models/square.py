#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class, inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ instatiates a square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ representas a square """
        return "[{}] ({}) {}/{} - {}".format(__class__.__name__, self.id,
                                             self.__x, self.__y, self.width)

    @property
    def size(self):
        """ property size """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if args and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary representation of a square """
        return {'id': self.id, 'size': self.width, 'x': self.__x,
                'y': self.__y}
