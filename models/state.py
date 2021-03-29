#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """ State class """    
    if storage_i == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    else:
        name = ""