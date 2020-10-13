#!/usr/bin/python3
"""Base Class"""


import json


class Base:
    """ This class will be the “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The goal of this is to manage id attribute in all your future
        classes and to avoid duplicating the same code"""
        # the id value is an identifier for each Base instance created
        if id is not None:
            self.id = id
        else:
            # you'll need to use the name of the class (Base) in order
            # to change the value of class variable __nb_objects
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries is a list
        of dictionaries """
        # on this case it returns the JSON string representation of
        # the empty list
        if list_dictionaries is None:
            # <class 'dict'>
            list_dictionaries = []
        # json.dumps returns the JSON string representation of the
        # parameter passed
        # list_dictionaries [{...(python object)},{...(python object)}]
        # el retorno es algo como "[{,,,(json representation object)},
        # {,,,(json representation object)}]"
        # <class 'str'>
        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        list_of_dictonaries = []

        # lists_objs is a list of instances who inherits of Base (List
        # of Rectangles or Squares)
        # si list_objs es None, guarde [save_to_file() guarde en el
        # archivo] una lista vacia...
        if list_objs is None:
            list_objs = []

        # antes de pasar los objetos a JSON, estos deben transladarse a
        # representaciones en Diccionarios para que puedan ser pasados
        # a JSON string
        for obj in list_objs:
            list_of_dictonaries.append(obj.to_dictionary())
        # El nombre del archivo debe ser: <Nombre de la clase>.json [el nombre
        # de la clase dependera de que typo sean las instancias que componen
        # la lista] - ejemplo: Rectangle.json
        file_name = "{}.json".format(cls.__name__)

        # debe usarse el metodo estatico to_json_string (creado anteriormente)
        # [lo que se va a guardar en el archivo es una representacion JSON
        # string de la lista de objetos]
        with open(file_name, mode="w", encoding="utf-8") as file_opened:
            return file_opened.write(cls.to_json_string(list_of_dictonaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string is (len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating new instances with all attributes"""
        # if the class name is equal to the "string"
        if cls.__name__ == "Rectangle":
            # the number of atributes corresponding to the instance are passed
            # atributes corresponding at Rectangle(width, height)
            new_instance = cls(4, 3)
            new_instance.update(**dictionary)
            return new_instance

        # if the class name is equal to the "string"
        if cls.__name__ == "Square":
            # attributes corresponding at Square(size)
            new_instance = cls(4)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Creates instances based on a list of instances from json file"""

        file_name = "{}.json".format(cls.__name__)
        try:
            list_instances = []
            with open(file_name, mode="r", encoding="utf-8") as file_opened:
                read_data = Base.from_json_string(file_opened.read())
                for dictionary in read_data:
                    list_instances.append(cls.create(**dictionary))
                return list_instances
        except IOError:
            return []
