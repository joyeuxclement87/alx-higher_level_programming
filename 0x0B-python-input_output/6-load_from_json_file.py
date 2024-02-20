#!/usr/bin/python3
"""function JSON file-reading to be defined"""
import json


def load_from_json_file(filename):
    """object in python to be created in json file"""
    with open(filename) as f:
        return json.load(f)
