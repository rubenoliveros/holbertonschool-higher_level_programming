#!/usr/bin/python3
"""
A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Defines whether the object is a an inherited class or not
    """
    return (isinstance(obj, a_class))
