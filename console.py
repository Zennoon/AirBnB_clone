#!/usr/bin/python3
"""
contains

classes:
    HBNBCommand - Implements the command interpreter for the project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Inherits from the Cmd class and implements the specific command interpreter.
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
