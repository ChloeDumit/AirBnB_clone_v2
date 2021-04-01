#!/usr/bin/python3
"""test for place"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "California"
        cls.city = City()
        cls.city.name = "San francisco"
        cls.city.state_id = "CA"
        cls.user = User()
        cls.user.first_name = "FN"
        cls.user.last_name = "LN"
        cls.user.email = "my@me"
        cls.user.password = "pwd"
        cls.place = Place()
        cls.place.city_id = "new city ID"
        cls.place.user_id = "new user ID"
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
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
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

    def test_save_State(self):
        """test if save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_save_City(self):
        """test if save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_save_User(self):
        """test if save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_save_Place(self):
        """test if save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)
