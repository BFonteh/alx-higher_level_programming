#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Function that read a text file and prnts it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
