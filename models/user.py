#!/usr/bin/python3
"""Contains User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Thus class will allows us to create user instances
    Args:
        BaseModel: A class to inherit from"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
