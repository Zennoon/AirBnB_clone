#!/usr/bin/python3
"""
contains

classes:
    HBNBCommand - Implements the command interpreter for the project
"""
import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Inherits from the Cmd class and implements the specific
    command interpreter.
    """
    prompt = "(hbnb) "
    class_names = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def empty_line(self):
        """
        Handles an empty line input.
        """
        pass

    def do_quit(self, line):
        """
        Handler for the quit command
        """
        return (True)

    def help_quit(self):
        """
        Displays the help message of the quit command.
        """
        print("Quits the command line interpreter")

    def do_EOF(self, line):
        """
        Handler for EOF (ctrl+D)
        """
        return (True)

    def help_EOF(self):
        """
        Displays the help message of the EOF command.
        """
        print("Exits the command line interpreter (when ctrl+d is clicked)")

    def emptyline(self):
        """
        Handles empty line input (empty line + ENTER)
        """
        pass

    """
    Action methods
    """
    def do_create(self, args):
        """
        creates a new instance and prints it's id
        """
        args = args.split(" ")
        if len(args) < 1 or not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        obj = HBNBCommand.class_names[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        loads and prints the string representation of an instance
        """
        args = args.split(" ")
        if len(args) < 1 or not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, args):
        """
        Destroys a class instance with a given ID.
        """
        args = args.split(" ")
        if len(args) < 1 or not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs_dct = storage.all()
        obj = objs_dct.get(key)
        if obj is None:
            print("** no instance found **")
            return
        del objs_dct[key]
        storage.save()

    def do_all(self, args):
        """
        Loads and prints the string representation of all instances of a model.
        """
        if args and args not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        output = []
        printed_classes = [args] if args else HBNBCommand.class_names
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if key.split(".")[0] in printed_classes:
                output.append(str(obj))
        print(output)

    def do_update(self, args):
        """
        Updates a given attribute of an instance of a given class.
        """
        args = args.split(" ")
        if len(args) < 1 or not args[0]:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        key = "{}.{}".format(args[0], args[1])
        objs_dct = storage.all()
        obj = objs_dct.get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[2] not in ["id", "created_at", "updated_at"]:
            # converting the value to the appropriate type
            if args[3][0] == '"':
                i = 4
                while args[3][-1] != '"':
                    args[3] += ' ' + args[i]
                    i += 1
            args[3] = args[3].strip('"\'')
            if obj.__dict__.get(args[2]) is not None:
                args[3] = type(obj.__dict__.get(args[2]))(args[3])
            else:
                args[3] = str(args[3])
            obj.__dict__[args[2]] = args[3]
            obj.save()

    def do_count(self, args):
        """
        counts the number of instance of a particular class
        """
        args = args.split(" ")
        count = 0
        all_keys = storage.all().keys()
        for key in all_keys:
            if args[0] in key:
                count += 1
        print(count)

    def default(self, args):
        """
        Default method
        """
        actions = {
                "all": self.do_all,
                "destroy": self.do_show,
                "update": self.do_update,
                "show": self.do_show,
                "count": self.do_count
                }

        args_split = re.split(r"[ .(),]", args)
        print(args_split)
        if len(args) > 1:
            for key in actions.keys():
                if key == args_split[1]:
                    if args_split[2] != "":
                        cleaned_args = args_split[2].replace('"', '')
                        params = f"{args_split[0]} {cleaned_args}"
                        return actions[args_split[1]](params)
                    else:
                        return actions[args_split[1]](args_split[0])

        print("** Unknown syntax: {}".format(args))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
