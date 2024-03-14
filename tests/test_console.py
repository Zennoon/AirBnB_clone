#!/usr/bin/python3
"""
contains

classes:
    TestHBNBCommand - unittest test cases for the HBNBCommand class/the console
"""
import io
import sys
import unittest
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """
    Contains test cases for the HBNBCommand class.
    """
    def setUp(self):
        """
        Set up code executed once before every test/method.
        """
        self.cmd = HBNBCommand()
        self.base = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def test_help(self):
        """
        Tests the help command.
        """
        w_space = "\n        {}\n        \n"

        # Tests -> help quit
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("help quit")
        text = "Quits the command line interpreter\n"
        self.assertEqual(output.getvalue(), text)
        output.close()

        # Tests -> help EOF
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("help EOF")
        text = "Exits the command line interpreter (when ctrl+d is clicked)\n"
        self.assertEqual(output.getvalue(), text)
        output.close()

        # Tests -> help create
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help create")
        text = "creates a new instance and prints it's id"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help show
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help show")
        text = "loads and prints the string representation of an instance"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help destroy
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help destroy")
        text = "Destroys a class instance with a given ID."
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help all
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help all")
        tmp = "of all instances of a model."
        text = "Loads and prints the string representation " + tmp
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help update
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help update")
        text = "Updates a given attribute of an instance of a given class."
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

        # Tests -> help count
        output = io.StringIO()
        sys.stdout = output
        HBNBCommand().onecmd("help count")
        text = "counts the number of instance of a particular class"
        self.assertEqual(output.getvalue(), w_space.format(text))
        output.close()

    def test_create(self):
        """
        Tests the create command of the HBNBCommand.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create BaseModel")
        key = "BaseModel.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], BaseModel)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create User")
        key = "User.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], User)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create State")
        key = "State.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], State)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create City")
        key = "City.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], City)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Amenity")
        key = "Amenity.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Amenity)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Place")
        key = "Place.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Place)

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Review")
        key = "Review.{}".format(output.getvalue().strip())
        self.assertTrue(key in storage.all())
        self.assertIsInstance(storage.all()[key], Review)

    def test_create_invalid_args(self):
        """
        Tests the create command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("create Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """
        Tests the show command of HBNBCommand class.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show BaseModel {}".format(self.base.id))
        self.assertEqual(output.getvalue(), str(self.base) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show User {}".format(self.user.id))
        self.assertEqual(output.getvalue(), str(self.user) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show State {}".format(self.state.id))
        self.assertEqual(output.getvalue(), str(self.state) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show City {}".format(self.city.id))
        self.assertEqual(output.getvalue(), str(self.city) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Amenity {}".format(self.amenity.id))
        self.assertEqual(output.getvalue(), str(self.amenity) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Place {}".format(self.place.id))
        self.assertEqual(output.getvalue(), str(self.place) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Review {}".format(self.review.id))
        self.assertEqual(output.getvalue(), str(self.review) + '\n')

    def test_show_invalid_args(self):
        """
        Tests the show command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("show User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """
        Tests the destroy command of the HBNBCommand class.
        """
        key = "BaseModel.{}".format(self.base.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy BaseModel {}".format(self.base.id))
        self.assertFalse(key in storage.all())

        key = "User.{}".format(self.user.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy User {}".format(self.user.id))
        self.assertFalse(key in storage.all())

        key = "State.{}".format(self.state.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy State {}".format(self.state.id))
        self.assertFalse(key in storage.all())

        key = "City.{}".format(self.city.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy City {}".format(self.city.id))
        self.assertFalse(key in storage.all())

        key = "Amenity.{}".format(self.amenity.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Amenity {}".format(self.amenity.id))
        self.assertFalse(key in storage.all())

        key = "Place.{}".format(self.place.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Place {}".format(self.place.id))
        self.assertFalse(key in storage.all())

        key = "Review.{}".format(self.review.id)
        self.assertTrue(key in storage.all())
        self.cmd.onecmd("destroy Review {}".format(self.review.id))
        self.assertFalse(key in storage.all())

    def test_destroy_invalid_args(self):
        """
        Tests the destroy command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("destroy User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

    def test_all(self):
        """
        Tests the all command of the HBNBCommand class.
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all")
        objs_lst = [str(obj) for obj in objs]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all BaseModel")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all User")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all State")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all City")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Amenity")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Place")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Review")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(objs_lst) + '\n')

    def test_all_invalid_args(self):
        """
        Tests the all command of the HBNBCommand class woth invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("all Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_update(self):
        """
        Tests the update command of the HBNBCommand class.
        """
        self.cmd.onecmd("update BaseModel {} name base".format(self.base.id))
        self.assertEqual(self.base.name, "base")

        self.cmd.onecmd("update User {} password pwd".format(self.user.id))
        self.assertEqual(self.user.password, "pwd")

        self.cmd.onecmd("update State {} name Arizona".format(self.state.id))
        self.assertEqual(self.state.name, "Arizona")

        command = "update City {} state_id {}"
        self.cmd.onecmd(command.format(self.city.id, self.state.id))
        self.assertEqual(self.city.state_id, self.state.id)

        self.cmd.onecmd("update Amenity {} name Pool".format(self.amenity.id))
        self.assertEqual(self.amenity.name, "Pool")

        command = "update Place {} city_id {}"
        self.cmd.onecmd(command.format(self.place.id, self.city.id))
        self.assertEqual(self.place.city_id, self.city.id)

        command = "update Review {} user_id {}"
        self.cmd.onecmd(command.format(self.review.id, self.user.id))
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_invalid_args(self):
        """
        Tests the update command of the HBNBCommand class with invalid args.
        """
        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update")
        self.assertEqual(output.getvalue(), "** class name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update Random")
        self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update BaseModel")
        self.assertEqual(output.getvalue(), "** instance id missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User 1234-4321-1234-4321")
        self.assertEqual(output.getvalue(), "** no instance found **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User {}".format(self.user.id))
        self.assertEqual(output.getvalue(), "** attribute name missing **\n")

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("update User {} first_name".format(self.user.id))
        self.assertEqual(output.getvalue(), "** value missing **\n")

    def test_count(self):
        """
        Tests the count command of the HBNBCommand class.
        """
        objs = storage.all().values()

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count BaseModel")
        objs_lst = [str(obj) for obj in objs if type(obj) is BaseModel]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count User")
        objs_lst = [str(obj) for obj in objs if type(obj) is User]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count State")
        objs_lst = [str(obj) for obj in objs if type(obj) is State]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count City")
        objs_lst = [str(obj) for obj in objs if type(obj) is City]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Amenity")
        objs_lst = [str(obj) for obj in objs if type(obj) is Amenity]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Place")
        objs_lst = [str(obj) for obj in objs if type(obj) is Place]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

        output = io.StringIO()
        sys.stdout = output
        self.cmd.onecmd("count Review")
        objs_lst = [str(obj) for obj in objs if type(obj) is Review]
        self.assertEqual(output.getvalue(), str(len(objs_lst)) + '\n')

    @classmethod
    def tearDownClass(cls):
        """
        Teardown method of the class, returns standard output to proper stream.
        """
        sys.stdout = sys.__stdout__
