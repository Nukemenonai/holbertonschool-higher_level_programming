#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ init method for square class
        Args:
            size: the size of the square
            position: a tuple containing x and y coordinates
        """
        tup = position
        if type(tup) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(tup[0]) is not int or type(tup[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif tup[0] < 0 or tup[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.position = position
            self.size = size

    def area(self):
        """ Gets the area of a square """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """ this function gets on my nerves. that is what it does. """
        return self.__size

    @size.setter
    def size(self, value):
        """ This function sets the size of the square. """
        if value < 0:
            raise ValueError('size must be >= 0')
        elif type(value) != int:
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    @property
    def position(self):
        """ function to get the position """
        return self.__position

    @position.setter
    def position(self, tup):
        """ This function sets the position
            Args:
                 tup: the tuple entered by the user
        """
        if type(tup) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(tup[0], int) or not isinstance(tup[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif tup[0] < 0 or tup[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = tup

    def my_print(self):
        """ Function to represent graphically the square"""
        if self.size == 0:
            print('')
        else:
            if self.__position[1] != 0:
                print('\n' * self.position[1], sep="", end="")
            for i in range(0, self.__size):
                print(" " * self.__position[0], sep="", end="")
                print("#" * self.__size, sep="")
