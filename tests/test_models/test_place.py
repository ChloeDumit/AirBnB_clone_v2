#!/usr/bin/python3
"""test for place"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "My_house"
        cls.place.description = "no_description_yet"
        cls.place.number_rooms = 4
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 3
        cls.place.price_by_night = 100
        cls.place.latitude = 120.12
        cls.place.longitude = 101.4
        cls.place.review = "cool"
        cls.place.amenity_ids = ["1324-efgh"]

    def test_attributes_Place(self):
        """tests if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "This test only work in Filestorage")
    def test_save_Place(self):
        """test if save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)
