#!/usr/binpython3
"""Defines a string to JSON function"""
import json

def in_json_strin(my_obj):
    """Return the JSON representation of a string object"""
    return json.dumps(my_obj)
