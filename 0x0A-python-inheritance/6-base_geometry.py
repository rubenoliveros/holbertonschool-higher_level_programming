#!/usr/bin/python3
"""
A class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    A class with area attribute that raises an exception 
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")
