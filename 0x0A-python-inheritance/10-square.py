#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from rectangle class"""

    def __init__(self, size):
        """ istantiates a square """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
