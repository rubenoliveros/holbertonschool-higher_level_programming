#!/usr/bin/python3
"""Function to find the peak of an array"""


def find_peak(list_of_integers):
    """Defines the function"""
    if list_of_integers == []:
        return None

    return print(list_of_integers.sort[-1])
