#!/usr/bin/python3
"""json-object function."""
import json


def from_json_string(my_str):
    """return python oject representation"""
    return json.loads(my_str)
