#!/usr/bin/python3
""" this module contains the class Base """
import json


class Base:
    """ empty Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for Base class
        Args:
            id (int): id for object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list of dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file - writes json string representation of list_objs
        Args:
            list_objs (list): list of objects
        """
        json_list = []
        json_string = '[]'
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

            if len(json_list) > 0:
                json_string = Base.to_json_string(json_list)

        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string representation
        Args:
            json_string (str): JSON string of object
        Returns:
            list of JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with attributes already set
        Args:
            dictionary (dict): dictionary of attributes and values
        Returns:
            instance of an object initialized
        """
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def reset(cls):
        """Reset __nb_objects back to zero"""
        cls.__nb_objects = 0

    @classmethod
    def load_from_file(cls):
        """ return list of instances
        Returns:
            list of instances
        """
        obj_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_output = cls.from_json_string(f.read())
                for obj in list_output:
                    obj_list.append(cls.create(**obj))
        except Exception:
            pass
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ csv format serialization """
        filename = cls.__name__ + ".csv"
        if cls.__name__ is "Rectangle":
            attrs = ["width", "height", "x", "y", "id"]
        elif cls.__name__ is "Square":
            attrs = ["size", "x", "y", "id"]
        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=attrs)
            if list_objs is not None:
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """ csv format deserialization """
        filename = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(filename, 'r', newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    new_list.append(row)
            return [cls.create(**obj) for obj in new_list]
        except FileNotFoundError:
            return [[]]
