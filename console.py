#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
       """Quit command to exit the program"""
       return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
