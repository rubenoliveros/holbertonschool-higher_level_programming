#!/usr/bin/python3
"""
A function that returns the list of available attributes
and methods of an object.
"""


def lookup(object):
    """
    List the attributes and methods that are currently available for an object
    """
    return dir(object)
