#!/usr/bin/python3
"""Contains FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """add new object to list of objects
        Args:
            obj: new object to be added"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        all_objs = FileStorage.__objects
        dic_objs = {obj: all_objs[obj].to_dict() for obj in all_objs.keys()}
        with open(FileStorage.__file_path, "w") as file_n:
            json.dump(dic_objs, file_n)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        try:
            with open(FileStorage.__file_path) as f_name:
                dic_objs = json.load(f_name)
                for ob in dic_objs.values():
                    class_n = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_n)(**ob))
        except:
            return
