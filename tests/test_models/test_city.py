#!/usr/bin/python3
"""
contains

classes:
    TestCity - unittest test cases for the City class
"""
import datetime
from models import storage
from models.base_model import BaseModel
import models.city
from models.state import State
import unittest


class TestCity(unittest.TestCase):
    """
    Contains test cases for the City class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.City = models.city.City

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.city = TestCity.City()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.city.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.City.__class__.__name__, "type")
        self.assertIsInstance(self.city, self.City)

    def test_attrs(self):
        """
        Tests that the attributes that are defined inside the City class exist.
        """
        self.assertTrue(hasattr(self.City, "state_id"))
        self.assertIsInstance(self.City.state_id, str)
        self.assertTrue(hasattr(self.City, "name"))
        self.assertIsInstance(self.City.name, str)

        self.city.name = "FirstCity"
        state = State()
        self.city.state_id = state.id

        self.assertEqual(self.city.name, "FirstCity")
        self.assertEqual(self.city.state_id, state.id)

    def test_inheritance(self):
        """
        Tests that the City class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.City, BaseModel))
        self.assertIsInstance(self.city, BaseModel)

    def test_super_init(self):
        """
        Tests that the attributes from the __init__ of BaseModel are in a City
        instance.
        """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertIsInstance(self.city.id, str)
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        city2 = TestCity.City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_str(self):
        """
        Tests the __str__ method of City instances.
        """
        output = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), output)

    def test_save(self):
        """
        Tests the save method of City instances.
        """
        old_upd_at = self.city.updated_at
        self.city.save()
        self.assertIsInstance(self.city.updated_at, datetime.datetime)
        self.assertNotEqual(self.city.updated_at, old_upd_at)
        self.assertTrue(self.city.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of City instances.
        """
        dct = self.city.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.city.__dict__)
        for key in self.city.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.city.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.city.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.city.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.city.__class__.__name__)

        self.city.name = "City Instance"
        self.city.number = 98
        dct = self.city.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "City Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.city.save()
        dct = self.city.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.city.updated_at)

        self.city.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.city.__class__.__name__, self.city.id)
        self.assertTrue(key in objs)
        city2 = objs[key]
        self.assertIsNot(self.city, city2)
        self.assertEqual(self.city.to_dict(), city2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.city.to_dict()
        city2 = TestCity.City("Unexpectedarguments", **dct)
        self.assertIsInstance(city2, TestCity.City)
        self.assertIsInstance(city2.created_at, datetime.datetime)
        self.assertIsInstance(city2.updated_at, datetime.datetime)
        self.assertIsNone(city2.__dict__.get("__class__"))
        dct2 = city2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.city), str(city2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        city2 = self.City()
        city2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(city2.__class__.__name__, city2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.City)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.city.to_dict()
        city2 = TestCity.City(**dct)
        self.assertIsNot(self.city, city2)
