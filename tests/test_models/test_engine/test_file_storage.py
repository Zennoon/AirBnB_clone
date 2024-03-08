#!/usr/bin/python3
"""
contains

classes:
    TestFileStorage - unittest test cases for the FileStorage class
"""
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Contains test cases for the FileStorage class.
    """
    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.storage = FileStorage()

    def test_private_attrs(self):
        """
        Tests that the private attributes can't be accessed with their names.
        """
        with self.assertRaises(AttributeError):
            objects = self.storage.__objects

        with self.assertRaises(AttributeError):
            file_path = self.storage.__file_path

    def test_all(self):
        """
        Tests the all method of FileStorage instances.
        """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        base = BaseModel()
        base.name = "Base model"
        base.number = 98
        all_objs = self.storage.all()
        self.assertNotEqual(all_objs, {})
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertTrue(key in all_objs)
        self.assertEqual(base.to_dict(), all_objs[key].to_dict())

    def test_new(self):
        """
        Tests the new method of FileStorage instances.
        """
        base = BaseModel()
        base.name = "Base model"
        base.number = 98
        all_objs = self.storage.all()
        self.assertNotEqual(all_objs, {})
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertTrue(key in all_objs)
        self.assertEqual(base.to_dict(), all_objs[key].to_dict())
        self.storage.new(base)
        new_objs = self.storage.all()
        # Doesn't insert the same object twice (no duplicate keys in a dict)
        self.assertEqual(new_objs, all_objs)
        base2 = BaseModel(**base.to_dict())
        new_objs = self.storage.all()
        self.assertEqual(new_objs, all_objs)

    def test_save(self):
        """
        Tests the save method of FileStorage instances.
        """
        base = BaseModel()
        self.storage.save()
        # Hardcoded filename used here
        with open("file.json", "rt", encoding="utf-8") as f:
            file_objs = json.load(f)

        all_objs = self.storage.all()
        self.assertIsInstance(file_objs, dict)
        for key in all_objs.keys():
            self.assertTrue(key in file_objs)
            self.assertIsInstance(file_objs[key], dict)

    def test_reload(self):
        """
        Tests the reload method of FileStorage instances.
        """
        self.storage.reload()
        all_objs = self.storage.all()
        self.storage.reload()
        new_objs = self.storage.all()
        self.assertEqual(all_objs.keys(), new_objs.keys())
        base = BaseModel()
        base.save()
        self.storage.reload()
        new_objs = self.storage.all()
        self.assertNotEqual(new_objs, all_objs)
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertTrue(key in new_objs)
