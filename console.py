#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parsing(arg):
    squares = re.search(r"\[(.*?)\]", arg)
    braces = re.search(r"\{(.*?)\}", arg)
    if braces is None:
        if squares is None:
            return [it.strip(",") for it in split(arg)]
        else:
            lxr = split(arg[:squares.span()[0]])
            rlt = [j.strip(",") for j in lxr]
            rlt.append(squares.group())
            return rlt
    else:
        lxr = split(arg[:braces.span()[0]])
        rlt = [j.strip(",") for j in lxr]
        rlt.append(braces.group())
        return rlt


class HBNBCommand(cmd.Cmd):
    """Class to handle the console
    Args: cmd.Cmd: Cmd class from cmd module"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    def emptyline(self):
        """Do Nothing"""
        pass

    def default(self, arg):
        """This will execute some default behavior when invalid input passed
        Args: arg: arguments"""
        dic_args = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        patt = re.search(r"\.", arg)
        if patt is not None:
            l_arg = [arg[:patt.span()[0]], arg[patt.span()[1]:]]
            patt = re.search(r"\((.*?)\)", l_arg[1])
            if patt is not None:
                comd = [l_arg[1][:patt.span()[0]], patt.group()[1:-1]]
                if comd[0] in dic_args.keys():
                    call = "{}.{}".format(l_arg[0], comd[1])
                    return dic_args[comd[0]](call)
            print("*** Unknown syntax: {}".format(arg))
            return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print('')
        return True

    def do_create(self, arg):
        """Creates a new instance
        Usage: create <class name>
        Args: arg: argument"""
        len_arg = parsing(arg)
        if len(len_arg) == 0:
            print("** class name missing **")
        elif len_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(len_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        Usage: show <class name> <instance id>
        Args: arg: arguments"""
        l_arg = parsing(arg)
        dic_objs = storage.all()
        if len(l_arg) == 0:
            print("** class name missing **")
        elif l_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l_arg[0], l_arg[1]) not in dic_objs:
            print("** no instance found **")
        else:
            print(dic_objs["{}.{}".format(l_arg[0], l_arg[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class name> <instance id>
        Args: arg: arguments"""
        l_arg = parsing(arg)
        dic_objs = storage.all()
        if len(l_arg) == 0:
            print("** class name missing **")
        elif l_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l_arg[0], l_arg[1]) not in dic_objs.keys():
            print("** no instance found **")
        else:
            del dic_objs["{}.{}".format(l_arg[0], l_arg[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        Usage: all Or all <class name>
        Args: arg: arguments"""
        l_arg = parsing(arg)
        if len(l_arg) > 0 and l_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            l_obj = []
            for ob in storage.all().values():
                if len(l_arg) > 0 and l_arg[0] == ob.__class__.__name__:
                    l_obj.append(ob.__str__())
                elif len(l_arg) == 0:
                    l_obj.append(ob.__str__())
            print(l_obj)

    def do_count(self, arg):
        """Get the number of instance of a class given
        Usage: count <class name>
        Args: arg: argument"""
        l_arg = parsing(arg)
        ct = 0
        for ob in storage.all().values():
            if len(l_arg) >= 1:
                if l_arg[0] == ob.__class__.__name__:
                    ct += 1
        print(ct)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        Usage: update <class name> <instance id> <name> <value>
        Args: arg: arguments"""
        l_arg = parsing(arg)
        dic_objs = storage.all()
        if len(l_arg) == 0:
            print("** class name missing **")
            return False
        if l_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(l_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(l_arg[0], l_arg[1]) not in dic_objs.keys():
            print("** no instance found **")
            return False
        if len(l_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(l_arg) == 3:
            try:
                type(eval(l_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(l_arg) == 4:
            obj = dic_objs["{}.{}".format(l_arg[0], l_arg[1])]
            if l_arg[2] in obj.__class__.__dict__.keys():
                type_v = type(obj.__class__.__dict__[l_arg[2]])
                obj.__dict__[l_arg[2]] = type_v(l_arg[3])
            else:
                obj.__dict__[l_arg[2]] = l_arg[3]
        elif type(eval(l_arg[2])) == dict:
            obj = dic_objs["{}.{}".format(l_arg[0], l_arg[1])]
            for k, v in eval(l_arg[2]).items():
                if (
                        k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}
                ):
                    type_v = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = type_v(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
