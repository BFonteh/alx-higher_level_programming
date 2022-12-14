#!/usr/bin/python3
"""Module 10-student"""


class Student:
    """ Defines a student instance"""

    def __init__(self, first_name, last_name, age):
        """ Initializes name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of a Student instance"""
        if isinstance(attrs, list) and all(
            map(lambda s: isinstance(s, str), attrs)
        ):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attrs of the Student instance"""
        self.__dict__.update(json)
