#!/usr/bin/python3
"""function JSON file-writing."""
import json


def save_to_json_file(my_obj, filename):
    """object to be written from JSON presentation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
