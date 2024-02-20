#!/usr/bin/python3
"""str-to-JSON function."""
import json


def to_json_string(my_obj):
    """JSON represantion of str oject."""
    return json.dumps(my_obj)
