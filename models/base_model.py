#!/usr/bin/python3
"""This module contains the base class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes an instance from the BaseModel
        Args:
            args: a tuple containing 0 or more arguments
            kwargs: a dictionary containing 0 or more k/v pairs"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if not kwargs:
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.today())
                    else:
                        setattr(self, k, v)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        new_dict = dict()
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    def __str__(self):
        """Modifies the behavior of dunder method str"""

        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
