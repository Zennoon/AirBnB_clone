#!/usr/bin/python3
"""
contains

classes:
    TestAmenity - unittest test cases for the Amenity class
"""
import datetime
from models import storage
from models.base_model import BaseModel
import models.amenity
from models.state import State
import unittest


class TestAmenity(unittest.TestCase):
    """
    Contains test cases for the Amenity class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.Amenity = models.amenity.Amenity

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.amenity = TestAmenity.Amenity()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.amenity.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.Amenity.__class__.__name__, "type")
        self.assertIsInstance(self.amenity, self.Amenity)

    def test_attrs(self):
        """
        Tests that attributes that are defined inside the Amenity class exist.
        """
        self.assertFalse(hasattr(self.Amenity, "state_id"))
        self.assertTrue(hasattr(self.Amenity, "name"))
        self.assertIsInstance(self.Amenity.name, str)

        self.amenity.name = "FirstAmenity"
        self.assertEqual(self.amenity.name, "FirstAmenity")

    def test_inheritance(self):
        """
        Tests that the Amenity class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.Amenity, BaseModel))
        self.assertIsInstance(self.amenity, BaseModel)

    def test_super_init(self):
        """
        Tests that the attributes from the __init__ of BaseModel are in a Amenity
        instance.
        """
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertIsInstance(self.amenity.id, str)
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        amenity2 = TestAmenity.Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_str(self):
        """
        Tests the __str__ method of Amenity instances.
        """
        am = self.Amenity()
        output = "[Amenity] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(str(am), output)

    def test_save(self):
        """
        Tests the save method of Amenity instances.
        """
        old_upd_at = self.amenity.updated_at
        self.amenity.save()
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)
        self.assertNotEqual(self.amenity.updated_at, old_upd_at)
        self.assertTrue(self.amenity.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of Amenity instances.
        """
        dct = self.amenity.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.amenity.__dict__)
        for key in self.amenity.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.amenity.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.amenity.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.amenity.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.amenity.__class__.__name__)

        self.amenity.name = "Amenity Instance"
        self.amenity.number = 98
        dct = self.amenity.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "Amenity Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.amenity.save()
        dct = self.amenity.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.amenity.updated_at)

        self.amenity.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.amenity.__class__.__name__, self.amenity.id)
        self.assertTrue(key in objs)
        amenity2 = objs[key]
        self.assertIsNot(self.amenity, amenity2)
        self.assertEqual(self.amenity.to_dict(), amenity2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.amenity.to_dict()
        amenity2 = TestAmenity.Amenity("Unexpectedarguments", **dct)
        self.assertIsInstance(amenity2, TestAmenity.Amenity)
        self.assertIsInstance(amenity2.created_at, datetime.datetime)
        self.assertIsInstance(amenity2.updated_at, datetime.datetime)
        self.assertIsNone(amenity2.__dict__.get("__class__"))
        dct2 = amenity2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.amenity), str(amenity2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        amenity2 = self.Amenity()
        amenity2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(amenity2.__class__.__name__, amenity2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.Amenity)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.amenity.to_dict()
        amenity2 = TestAmenity.Amenity(**dct)
        self.assertIsNot(self.amenity, amenity2)
