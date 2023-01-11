#!/usr/bin/python3
"""Module 100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each search_string"""
    with open(filename, mode='r+') as f:
        lines = [
            line + new_string * (search_string in line)
            for line in f.readlines()
        ]
        f.seek(0)
        f.writelines(lines)
