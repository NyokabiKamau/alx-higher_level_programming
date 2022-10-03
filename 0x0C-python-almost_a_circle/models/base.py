#!/urs/bin/python3

"""This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code
"""
import json
import os
import csv

class Base:
    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilization of base instance
        Args:
            - id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON rep of list_dictionaries
        Args:
        - list_dictionaries: string to be represented
        Returns: JSON representation
        """
        if list_dictionaries == None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
