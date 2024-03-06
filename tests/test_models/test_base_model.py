#!/usr/bin/python3
"""
contains

classes:
    TestBaseModel - unittest test cases for the BaseModel class
"""
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

    
