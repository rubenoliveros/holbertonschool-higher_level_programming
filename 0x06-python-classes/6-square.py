#!/usr/bin/python3
"""A class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """Declares the class Square"""
    def __init__(self, size=0):
        """Initializates tha class"""
        self.size = size

    def area(self):
        """Defines the class area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """Declares the getter for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Declares the setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

    @property
    def position(self):
        """getter of __position"""

    @position.setter
    def position(self, value):
        """setter of __position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
