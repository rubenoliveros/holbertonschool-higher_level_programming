#!/usr/bin/python3
"""
A a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""


class Rectangle:
    """
    Defines a function called Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that calculates the perimeter"""
        if self.__width == 0 or self.__height == 0:
        return self.__width * self.__height

    def perimeter(self):
        """Function that calculates the perimeter"""
        if self.__width == 0 or self.__height == 0:
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Function that prints the rectangle"""
        pixel = ""
        if self.__width == 0 or self.__height == 0:
            return pixel
        for i in range(self.__height):
            for j in range(self.__width):
                pixel += "#"
            if i is not self.__height:
                pixel += "\n"
        return pixel

    def __repr__(self):
        """Function that helps to recreate a new instance of the class"""
 
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
