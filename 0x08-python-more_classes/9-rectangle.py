#!/usr/bin/python3
class Rectangle:
    """ Defines a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init method for my class
       args:
           width:
           height:
        """
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width property of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """Init method for rectangle class
        Args:
        width: width of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """property height for rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """ defines the heigh of the rectangle"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """defines the area of my rectangle"""
        if self.__width == 0 or self.__height == 0:
            area = 0
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        """ defines the perimeter of my rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return (perimeter)

    def __str__(self):
        "string representation of a rectangle"
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            row = str(self.print_symbol) * self.__width
            return '\n'.join([str(row)] * self.__height)

    def __repr__(self):
        """ represents a square """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ deletes instance of a rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        print("area of rectangle 1 is {}".format(rect_1.area()))
        print("area of rectangle 2 is {}".format(rect_2.area()))
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """ the info given is sent to parent class for verification"""
        return Rectangle(size, size)
