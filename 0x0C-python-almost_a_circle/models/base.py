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
        
        @classmethod
        def save_to_file(cls, list_objs):
            """writes the JSON string rep of list_objs
            Args:
            - list_objs is a list of instances who inherits of Base
            e.g list of Rectangle
            """
            if list_objs is None or lists_objs == "[]":
                jstring = "[]"
            else:
                jstring = cls.to_json_string([o.to_dictionary() for o in list_objs])
            filename = cls.__name__ + ".json"
            with open(filename, 'w') as jfile:
                jfile.write(jstring)
        
        @staticmethod
        def from_json_string(json_string):
            """Returns the list of the JSON string rep of json_string
            Args:
                - json_string: string to convert
            """
            if json_string is None or json_string == "[]":
                return []
            return json.loads(json_string)

        @classmethod
        def create(clc, **dictionary):
            """returns an instance with all attributes already set
            Args:
                - dictionary: used as **kwargs
            """
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

        @class
