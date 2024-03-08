#!/usr/bin/python3
"""
contains

classes:
    TestState - unittest test cases for the State class
"""
import datetime
from models import storage
from models.base_model import BaseModel
import models.state
import unittest


class TestState(unittest.TestCase):
    """
    Contains test cases for the State class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.State = models.state.State

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.state = TestState.State()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.state.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.State.__class__.__name__, "type")
        self.assertIsInstance(self.state, self.State)

    def test_attrs(self):
        """
        Tests that the attributes that are defined inside the State class exist.
        """
        self.assertTrue(hasattr(self.State, "name"))
        self.assertIsInstance(self.State.name, str)

        self.state.name = "SomeState"

        self.assertEqual(self.state.name, "SomeState")

    def test_inheritance(self):
        """
        Tests that the State class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.State, BaseModel))
        self.assertIsInstance(self.state, BaseModel)

    def test_super_init(self):
        """
        Tests that the attributes from the __init__ of BaseModel are in a State
        instance.
        """
        self.assertTrue(hasattr(self.state, "id"))
        self.assertIsInstance(self.state.id, str)
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        state2 = TestState.State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_str(self):
        """
        Tests the __str__ method of State instances.
        """
        output = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), output)

    def test_save(self):
        """
        Tests the save method of State instances.
        """
        old_upd_at = self.state.updated_at
        self.state.save()
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        self.assertNotEqual(self.state.updated_at, old_upd_at)
        self.assertTrue(self.state.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of State instances.
        """
        dct = self.state.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.state.__dict__)
        for key in self.state.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.state.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.state.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.state.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.state.__class__.__name__)

        self.state.name = "State Instance"
        self.state.number = 98
        dct = self.state.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "State Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.state.save()
        dct = self.state.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.state.updated_at)

        self.state.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.state.__class__.__name__, self.state.id)
        self.assertTrue(key in objs)
        state2 = objs[key]
        self.assertIsNot(self.state, state2)
        self.assertEqual(self.state.to_dict(), state2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.state.to_dict()
        state2 = TestState.State("Unexpectedarguments", **dct)
        self.assertIsInstance(state2, TestState.State)
        self.assertIsInstance(state2.created_at, datetime.datetime)
        self.assertIsInstance(state2.updated_at, datetime.datetime)
        self.assertIsNone(state2.__dict__.get("__class__"))
        dct2 = state2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.state), str(state2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        state2 = self.State()
        state2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(state2.__class__.__name__, state2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.State)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.state.to_dict()
        state2 = TestState.State(**dct)
        self.assertIsNot(self.state, state2)
