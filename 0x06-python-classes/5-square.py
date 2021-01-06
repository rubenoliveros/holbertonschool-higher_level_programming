#!/usr/bin/python3
"""A class Square that defines a square by: (based on 4-square.py)"""


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
