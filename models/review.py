#!/usr/bin/python3
"""Contains class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review to create review instances
    Args:
        BaseModel: Mother class"""
    place_id = ""
    user_id = ""
    text = ""
