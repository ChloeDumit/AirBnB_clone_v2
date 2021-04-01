#!/usr/bin/python3

""" test for city"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """this will test the city class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "This test only work in Filestorage")
    def test_state_id(self):
        """tests attr type """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "This test only work in Filestorage")
    def test_name(self):
        """tests attr type """
        new = self.value()
        self.assertEqual(type(new.name), str)
