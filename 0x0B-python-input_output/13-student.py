#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary
        representation of a Student instance"""

        if attrs is None:
            return self.__dict__

        flag_instance = 0
        for atribute in attrs:
            if not isinstance(atribute, str):
                flag_instance = 1

        if flag_instance == 0:
            dic_to_return = {}
            for key in attrs:
                try:
                    dic_to_return[key] = self.__dict__[key]
                except:
                    pass
            return dic_to_return

        return self.__dict__

    def reload_from_json(self, json):
        """Public method that replaces all
        attributes of the Student instance"""

        for key in json:
            self.__dict__[key] = json[key]
