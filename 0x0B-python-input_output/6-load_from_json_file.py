#!/usr/bin/python3
"""Module 6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """Function creates object from JSON fle"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
