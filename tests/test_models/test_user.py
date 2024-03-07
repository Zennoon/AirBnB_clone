#!/usr/bin/python3
"""
contains

classes:
    TestUser - unittest test cases for the User class
"""
import datetime
from models import storage
from models.base_model import BaseModel
import models.user
import unittest


class TestUser(unittest.TestCase):
    """
    Contains test cases for the User class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.User = models.user.User

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.user = TestUser.User()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.user.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.User.__class__.__name__, "type")
        self.assertIsInstance(self.user, self.User)

    def test_attrs(self):
        """
        Tests that the attributes that are defined inside the User class exist.
        """
        self.assertTrue(hasattr(self.User, "email"))
        self.assertIsInstance(self.User.email, str)
        self.assertTrue(hasattr(self.User, "password"))
        self.assertIsInstance(self.User.password, str)
        self.assertTrue(hasattr(self.User, "first_name"))
        self.assertIsInstance(self.User.first_name, str)
        self.assertTrue(hasattr(self.User, "last_name"))
        self.assertIsInstance(self.User.last_name, str)

        self.user.first_name = "FirstUser"
        self.user.last_name = "User"
        self.user.email = "firstuser@User.com"
        self.user.password = "root"

        self.assertEqual(self.user.first_name, "FirstUser")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.email, "firstuser@User.com")
        self.assertEqual(self.user.password, "root")

    def test_inheritance(self):
        """
        Tests that the User class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)

    def test_super_init(self):
        """
        Tests that the attributes from the __init__ of BaseModel are in a User
        instance.
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertIsInstance(self.user.id, str)
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        user2 = TestUser.User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_str(self):
        """
        Tests the __str__ method of User instances.
        """
        output = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), output)

    def test_save(self):
        """
        Tests the save method of User instances.
        """
        old_upd_at = self.user.updated_at
        self.user.save()
        self.assertIsInstance(self.user.updated_at, datetime.datetime)
        self.assertNotEqual(self.user.updated_at, old_upd_at)
        self.assertTrue(self.user.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of User instances.
        """
        dct = self.user.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.user.__dict__)
        for key in self.user.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.user.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.user.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.user.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.user.__class__.__name__)

        self.user.name = "User Instance"
        self.user.number = 98
        dct = self.user.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "User Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.user.save()
        dct = self.user.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.user.updated_at)

        self.user.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertTrue(key in objs)
        user2 = objs[key]
        self.assertIsNot(self.user, user2)
        self.assertEqual(self.user.to_dict(), user2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.user.to_dict()
        user2 = TestUser.User("Unexpectedarguments", **dct)
        self.assertIsInstance(user2, TestUser.User)
        self.assertIsInstance(user2.created_at, datetime.datetime)
        self.assertIsInstance(user2.updated_at, datetime.datetime)
        self.assertIsNone(user2.__dict__.get("__class__"))
        dct2 = user2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.user), str(user2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        user2 = self.User()
        user2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(user2.__class__.__name__, user2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.User)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.user.to_dict()
        user2 = TestUser.User(**dct)
        self.assertIsNot(self.user, user2)
