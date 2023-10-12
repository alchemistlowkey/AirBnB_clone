#!/usr/bin/python3
"""
The Command Interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter
    """

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
