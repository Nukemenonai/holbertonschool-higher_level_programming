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
