#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0,0)):
        """ init method for square class

        Args:
            size: the size of the square
            position: a tuple containing x and y coordinates
        """
        try:
            if size < 0:
                raise ValueError
            elif type(size) != int:
                raise TypeError(i)
            elif type(position) != tuple:
                raise TypeError(tup)
            elif position[0] < 0 or position[1] < 0:
                raise TypeError(tup)
            else:
                self.__size = size
                self.__position = position
        except TypeError(i):
            raise TypeError("size must be an integer")
        except TypeError(tup):
            raise TypeError("position must be a tuple of 2 positive integers")
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
        """ This function sets the size of the square. """
        if x < 0:
            raise ValueError
        elif type(x) != int:
            raise TypeError
        else:
            self.__size = x

    @property
    def position(self):
        """ function to get the position """
        return self.__position

    @position.setter
    def position(self, tup):
        """ This function sets the position """
        if type(position) != tuple:
            raise TypeError(tup)
        elif position[0] < 0 or position[1] < 0:
            raise TypeError(tup)
        else:
            self.__position = tup


    def my_print(self):
        """ Function to represent graphically the square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                if self.__position[1] == 0:
                    print(" " * self.__position[0], sep="", end="")
                print("#" * self.__size, sep="")
