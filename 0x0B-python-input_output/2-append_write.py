#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """Function that appends a string to a text file
    Returns:
        number of characters written
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)

    return len(text)
