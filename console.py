#!/usr/bin/env python3
"""
Console module for the HBNB project
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class - command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel or User"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objs = storage.all()
        if not arg:
            print([str(objs[key]) for key in objs])
            return
        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        print([str(objs[key]) for key in objs if key.startswith(arg + ".")])

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], eval(args[3]))
        objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
