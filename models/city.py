#!/usr/bin/python3
"""Contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City to create city instances
    Args:
        BaseModel: Mother class"""
    state_id = ""
    name = ""
