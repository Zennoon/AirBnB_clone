#!/usr/bin/python3
"""
contains

classes:
    TestBaseModel - unittest test cases for the BaseModel class
"""
import datetime
import models.base_model
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Contains test cases for the BaseModel class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.BaseModel = models.base_model.BaseModel

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.base = TestBaseModel.BaseModel()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.base_model.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.BaseModel.__class__.__name__, "type")
        self.assertIsInstance(self.base, self.BaseModel)

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        with self.assertRaises(TypeError):
            b = TestBaseModel.BaseModel("Unexpectedarguments")

    def test_attrs(self):
        """
        Tests the existence and validity of instance attributes.
        """
        self.assertTrue(hasattr(self.base, "id"))
        self.assertIsInstance(self.base.id, str)
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
        self.assertFalse(hasattr(self.base, "random"))
        self.base.name = "A BaseModel Instance"
        self.assertTrue(hasattr(self.base, "name"))
        self.assertEqual(self.base.name, "A BaseModel Instance")

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        base2 = TestBaseModel.BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_str(self):
        """
        Tests the __str__ method of BaseModel instances.
        """
        output = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), output)

    def test_save(self):
        """
        Tests the save method of BaseModel instances.
        """
        old_upd_at = self.base.updated_at
        self.base.save()
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
        self.assertNotEqual(self.base.updated_at, old_upd_at)
        self.assertTrue(self.base.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of BaseModel instances.
        """
        dct = self.base.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.base.__dict__)
        for key in self.base.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.base.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at\
"])
        self.assertEqual(created_at, self.base.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.base.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.base.__class__.__name__)

        self.base.name = "BaseModel Instance"
        self.base.number = 98
        dct = self.base.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "BaseModel Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.base.save()
        dct = self.base.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.base.updated_at)
