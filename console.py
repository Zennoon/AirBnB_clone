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
        if len(args) < 1:
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
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("**instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, args):
        """
        Destroys a class instance with a given ID
        """
        args = args.split(" ")
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_names.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("**instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs_dct = storage.all()
        obj = objs_dct.get(key)
        if obj is None:
            print("** no instance found **")
            return
        del objs_dct[key]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
