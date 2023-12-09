#!/usr/bin/python3
"""Contains User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Thus class will allows us to create user instances
    Args:
        BaseModel: A class to inherit from
    Attributes:
        email: the user email
        password: the user password
        first_name: the first name of the user
        last_name: the last name of the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
