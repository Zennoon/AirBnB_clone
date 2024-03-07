#!/usr/bin/python3
"""
contains

classes:
    HBNBCommand - Implements the command interpreter for the project
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Inherits from the Cmd class and implements the specific
    command interpreter.
    """
    prompt = "(hbnb) "
    class_names = {"BaseModel": BaseModel}

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
            args[3] = args[3].strip('"')
            if obj.__dict__.get(args[2]) is not None:
                args[3] = type(obj.__dict__.get(args[2]))(args[3])
            else:
                args[3] = str(args[3])
            obj.__dict__[args[2]] = args[3]
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
