#!/usr/bin/python3
"""
contains

classes:
    TestReview - unittest test cases for the.Review class
"""
import datetime
from models import storage
from models.base_model import BaseModel
import models.review
from models.place import Place
from models.user import User
import unittest


class TestReview(unittest.TestCase):
    """
    Contains test cases for the Review class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up code executed before the test cases.
        """
        cls.Review = models.review.Review

    def setUp(self):
        """
        Set up code executed before each test/method.
        """
        self.review = TestReview.Review()

    def test_module(self):
        """
        Tests that the module has been imported correctly.
        """
        self.assertEqual(models.review.__class__.__name__, "module")

    def test_class(self):
        """
        Tests that the class has been imported correctly.
        """
        self.assertEqual(self.Review.__class__.__name__, "type")
        self.assertIsInstance(self.review, self.Review)

    def test_attrs(self):
        """
        Tests that attributes that are defined inside the Review class exist.
        """
        self.assertTrue(hasattr(self.Review, "user_id"))
        self.assertIsInstance(self.Review.user_id, str)
        self.assertTrue(hasattr(self.Review, "place_id"))
        self.assertIsInstance(self.Review.place_id, str)
        self.assertTrue(hasattr(self.Review, "text"))
        self.assertIsInstance(self.Review.text, str)

        place = Place()
        user = User()
        self.review.user_id = user.id
        self.review.place_id = place.id
        dct = storage.all()
        place_key = "Place.{}".format(place.id)
        user_key = "User.{}".format(user.id)
        self.review.text = "The place is awesome"

        self.assertEqual(self.review.place_id, dct[place_key].id)
        self.assertEqual(self.review.user_id, dct[user_key].id)
        self.assertEqual(self.review.text, "The place is awesome")

    def test_inheritance(self):
        """
        Tests that the Review class inherits from the BaseModel class.
        """
        self.assertTrue(issubclass(self.Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_super_init(self):
        """
        Tests that the attributes from the __init__ of BaseModel are in a Review
        instance.
        """
        self.assertTrue(hasattr(self.review, "id"))
        self.assertIsInstance(self.review.id, str)
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Tests that different instances have different ids.
        """
        review2 = TestReview.Review()
        self.assertNotEqual(self.review.id, review2.id)

    def test_str(self):
        """
        Tests the __str__ method of Review instances.
        """
        output = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), output)

    def test_save(self):
        """
        Tests the save method of Review instances.
        """
        old_upd_at = self.review.updated_at
        self.review.save()
        self.assertIsInstance(self.review.updated_at, datetime.datetime)
        self.assertNotEqual(self.review.updated_at, old_upd_at)
        self.assertTrue(self.review.updated_at > old_upd_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of Review instances.
        """
        dct = self.review.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIsNot(dct, self.review.__dict__)
        for key in self.review.__dict__.keys():
            self.assertIsNotNone(dct.get(key))

        self.assertEqual(dct["id"], self.review.id)
        created_at = datetime.datetime.fromisoformat(dct["created_at"])
        self.assertEqual(created_at, self.review.created_at)
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.review.updated_at)
        self.assertIsNotNone(dct.get("__class__"))
        self.assertEqual(dct.get("__class__"), self.review.__class__.__name__)

        self.review.name = "Review Instance"
        self.review.number = 98
        dct = self.review.to_dict()
        self.assertIsNotNone(dct.get("name"))
        self.assertEqual(dct.get("name"), "Review Instance")
        self.assertIsNotNone(dct.get("number"))
        self.assertEqual(dct.get("number"), 98)

        self.review.save()
        dct = self.review.to_dict()
        updated_at = datetime.datetime.fromisoformat(dct["updated_at"])
        self.assertEqual(updated_at, self.review.updated_at)

        self.review.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(self.review.__class__.__name__, self.review.id)
        self.assertTrue(key in objs)
        review2 = objs[key]
        self.assertIsNot(self.review, review2)
        self.assertEqual(self.review.to_dict(), review2.to_dict())

    def test_args(self):
        """
        Tests the class when unexpected arguments are provided.
        """
        dct = self.review.to_dict()
        review2 = TestReview.Review("Unexpectedarguments", **dct)
        self.assertIsInstance(review2, TestReview.Review)
        self.assertIsInstance(review2.created_at, datetime.datetime)
        self.assertIsInstance(review2.updated_at, datetime.datetime)
        self.assertIsNone(review2.__dict__.get("__class__"))
        dct2 = review2.to_dict()
        for key in dct.keys():
            self.assertIsNotNone(dct2.get(key))
            self.assertEqual(dct[key], dct2[key])
        self.assertEqual(str(self.review), str(review2))

    def test_identity(self):
        """
        Tests that reloading the objects persists the type of objects.
        """
        review2 = self.Review()
        review2.save()
        storage.reload()
        all_objs = storage.all()
        key = "{}.{}".format(review2.__class__.__name__, review2.id)
        self.assertTrue(key in all_objs)
        self.assertIsInstance(all_objs[key], self.Review)

    def test_equality(self):
        """
        Tests that two instances with identical attributes are not the same.
        """
        dct = self.review.to_dict()
        review2 = TestReview.Review(**dct)
        self.assertIsNot(self.review, review2)
