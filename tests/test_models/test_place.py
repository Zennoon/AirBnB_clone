#!/usr/bin/python3
"""
contains

classes:
    TestPlace - unittest test cases for the Place class
"""
import datetime
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
import models.place
import unittest


class TestPlace(unittest.TestCase):
    """
    Contains test cases for the Place class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.Place = models.place.Place

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.place = TestPlace.Place()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.place.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.Place.__class__.__name__, "type")
        self.assertIsInstance(self.place, self.Place)

    def test_attrs(self):
        """
        Tests that attributes that are defined inside the Place class exist.
        """
        self.assertTrue(hasattr(self.Place, "city_id"))
        self.assertIsInstance(self.Place.city_id, str)
        self.assertTrue(hasattr(self.Place, "user_id"))
        self.assertIsInstance(self.Place.user_id, str)
        self.assertTrue(hasattr(self.Place, "name"))
        self.assertIsInstance(self.Place.name, str)
        self.assertTrue(hasattr(self.Place, "description"))
        self.assertIsInstance(self.Place.description, str)
        self.assertTrue(hasattr(self.Place, "number_rooms"))
        self.assertIsInstance(self.Place.number_rooms, int)
        self.assertTrue(hasattr(self.Place, "number_bathrooms"))
        self.assertIsInstance(self.Place.number_bathrooms, int)
        self.assertTrue(hasattr(self.Place, "price_by_night"))
        self.assertIsInstance(self.Place.price_by_night, int)
        self.assertTrue(hasattr(self.Place, "max_guest"))
        self.assertIsInstance(self.Place.max_guest, int)
        self.assertTrue(hasattr(self.Place, "latitude"))
        self.assertIsInstance(self.Place.latitude, float)
        self.assertTrue(hasattr(self.Place, "longitude"))
        self.assertIsInstance(self.Place.longitude, float)
        self.assertTrue(hasattr(self.Place, "amenity_ids"))
        self.assertIsInstance(self.Place.amenity_ids, list)

        city = City()
        user = User()
        amenity1 = Amenity()
        amenity2 = Amenity()
        dct = storage.all()
        self.place.city_id = city.id
        self.place.user_id = user.id
        self.place.name = "Place"
        self.place.description = "Just a place"
        self.place.number_rooms = 8
        self.place.number_bathrooms = 3
        self.place.max_guest = 6
        self.place.price_by_night = 1000
        self.place.latitude = 65.2345
        self.place.longitude = 87.1264
        self.place.amenity_ids.append(amenity1.id)
        self.place.amenity_ids.append(amenity2.id)

        city_key = "City.{}".format(city.id)
        user_key = "User.{}".format(user.id)
        amenity1_key = "Amenity.{}".format(amenity1.id)
        amenity2_key = "Amenity.{}".format(amenity2.id)
        self.assertEqual(self.place.city_id, dct[city_key].id)
        self.assertEqual(self.place.user_id, dct[user_key].id)
        self.assertEqual(self.place.name, "Place")
        self.assertEqual(self.place.description, "Just a place")
        self.assertEqual(self.place.number_rooms, 8)
        self.assertEqual(self.place.number_bathrooms, 3)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 1000)
        self.assertEqual(self.place.latitude, 65.2345)
        self.assertEqual(self.place.longitude, 87.1264)
        self.assertEqual(self.place.amenity_ids[0], dct[amenity1_key].id)
        self.assertEqual(self.place.amenity_ids[1], dct[amenity2_key].id)

    def test_inheritance(self):
        """
        Tests that the Place class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.Place, BaseModel))
        self.assertIsInstance(self.place, BaseModel)

    def test_super_init(self):
        """
        Tests that attributes from the __init__ of BaseModel are in a Place
        instance.
        """
        self.assertTrue(hasattr(self.place, "id"))
        self.assertIsInstance(self.place.id, str)
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertIsInstance(self.place.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        place2 = TestPlace.Place()
        self.assertNotEqual(self.place.id, place2.id)

    def test_str(self):
        """
        Tests the __str__ method of Place instances.
        """
        output = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), output)

    def test_save(self):
        """
        Tests the save method of Place instances.
        """
        old_upd_at = self.place.updated_at
        self.place.save()
        self.assertIsInstance(self.place.updated_at, datetime.datetime)
        self.assertNotEqual(self.place.updated_at, old_upd_at)
        self.assertTrue(self.place.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of Place instances.
        """
        dct = self.place.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.place.__dict__)
        for key in self.place.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.place.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.place.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.place.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.place.__class__.__name__)

        self.place.name = "Place Instance"
        self.place.number = 98
        dct = self.place.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "Place Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.place.save()
        dct = self.place.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.place.updated_at)

        self.place.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.place.__class__.__name__, self.place.id)
        self.assertTrue(key in objs)
        place2 = objs[key]
        self.assertIsNot(self.place, place2)
        self.assertEqual(self.place.to_dict(), place2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.place.to_dict()
        place2 = TestPlace.Place("Unexpectedarguments", **dct)
        self.assertIsInstance(place2, TestPlace.Place)
        self.assertIsInstance(place2.created_at, datetime.datetime)
        self.assertIsInstance(place2.updated_at, datetime.datetime)
        self.assertIsNone(place2.__dict__.get("__class__"))
        dct2 = place2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.place), str(place2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        place2 = self.Place()
        place2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(place2.__class__.__name__, place2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.Place)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.place.to_dict()
        place2 = TestPlace.Place(**dct)
        self.assertIsNot(self.place, place2)
