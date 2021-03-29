#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

storage_i = getenv("HBNB_TYPE_STORAGE")
if storage_i == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
