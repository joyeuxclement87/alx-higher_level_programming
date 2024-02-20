#!/usr/bin/python3
"""student class"""


class Student:
    """student to be reprsented"""

    def __init__(self, first_name, last_name, age):
        """new student to be initialize

        Args:
            first_name (str): student first name
            last_name (str): last name student
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary of represent of student"""
        return self.__dict__
