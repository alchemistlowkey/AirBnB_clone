#!/usr/bin/python3
"""
The Command Interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """

    prompt = "(hbnb) "

    classes = {
            "BaseModel"
            }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """

        return True

    def do_EOF(self, line):
        """
        End of File to exit using ctrl d
        """

        print("")
        return True

    def emptyline(self):
        """
        Empty line command to do nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance
        """

        cmd_line = arg.split()
        if not self.class_verify(cmd_line):
            return
        count = eval(cmd_line[0] + "()")
        if isinstance(count, BaseModel):
            count.save()
            print(count.id)
        return

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        cmd_line = arg.split()
        if not self.class_verify(cmd_line):
            return
        if not self.id_verify(cmd_line):
            return
        key = "{}.{}".format(cmd_line[0], cmd_line[1])
        obj = storage.all()
        print(obj[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """

        cmd_line = arg.split()
        if not self.class_verify(cmd_line):
            return
        if not self.id_verify(cmd_line):
            return
        key = "{}.{}".format(cmd_line[0], cmd_line[1])
        obj = storage.all()
        del obj[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        cmd_line = arg.split()
        if len(cmd_line) > 0 and cmd_line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            holder = []
            for val in obj.values():
                if len(cmd_line) > 0 and cmd_line[0] == val.__class__.__name__:
                    holder.append(val.__str__())
                elif len(cmd_line) == 0:
                    holder.append(val.__str__())
            print(holder)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """

        cmd_line = arg.split()
        if not self.class_verify(cmd_line):
            return
        if not self.id_verify(cmd_line):
            return
        if not self.attr_verify(cmd_line):
            return
        key = "{}.{}".format(cmd_line[0], cmd_line[1])
        obj = storage.all()
        setattr(obj[key], cmd_line[2], cmd_line[3])
        storage.save()

    @classmethod
    def class_verify(cls, line):
        """
        Class method to verify class
        """
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def id_verify(line):
        """
        Static method to verify id.
        """
        if len(line) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        key = "{}.{}".format(line[0], line[1])
        if key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def attr_verify(line):
        """
        Static method to verify the attribute
        """
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
