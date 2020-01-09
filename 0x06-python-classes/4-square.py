#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """ init method for square class

        Args:
            Size: the size of the square
        """
        try:
            if size < 0:
                raise ValueError
            elif type(size) != int:
                raise TypeError
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Gets the area of a square """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """ this function gets on my nerves. that is what it does. """
        return self.__size

    @size.setter
    def size(self, x):
        try:
            if x < 0:
                raise ValueError
            elif type(x) != int:
                raise TypeError
            else:
                self.__size = x
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
