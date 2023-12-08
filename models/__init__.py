#!/usr/bin/python3
"""init module to make models a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
