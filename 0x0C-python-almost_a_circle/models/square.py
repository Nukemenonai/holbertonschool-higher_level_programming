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
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

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
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary representation of a square """
        return {'id': self.id, 'size': self.width, 'x': self.__x,
                'y': self.__y}
