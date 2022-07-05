#!/usr/bin/python3
"""Defines a json file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using json representation"""
    with open(filename, "s") as d:
        json.dump(my_obj, d)
