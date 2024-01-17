#!/usr/bin/python3
"""
Console Module: Defines the HBNBCommand class for the command-line interface.
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Contains the functionality for the HBNB console.

    Attributes:
        prompt (str): The prompt shown to the user in interactive mode.
        classes (dict): A mapping of class names to class objects.
        dot_cmds (list): A list of commands that start with a dot.
        types (dict): A mapping of attribute names to data types.
    """

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }
    dot_cmds = ["all", "count", "show", "destroy", "update"]
    types = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    def preloop(self):
        """
        Prints if isatty is false
        """
        # New variable to store the status of the standard input
        is_interactive = sys.__stdin__.isatty()

        # Check if the standard input is not interactive
        if not is_interactive:
            print("(hbnb)")

    def precmd(self, line):
        """
        Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)

        Args:
            self: The instance of the `HBNBCommand` class.
            line (str): The command line input.

        Returns:
            str: The reformatted command line.
        """
        # New variables to store the command, class, id, and arguments
        _cmd = _cls = _id = _args = ""

        # New variable to store the parsed line
        pline = line[:]

        # Check for general formatting - i.e '.', '(', ')'
        if "." in line and "(" in line and ")" in line:
            try:
                # Isolate <class name>
                _cls = pline[: pline.find(".")]

                # Isolate and validate <command>
                _cmd = pline[pline.find(".") + 1 : pline.find("(")]
                if _cmd not in HBNBCommand.dot_cmds:
                    raise Exception

                # If parentheses contain arguments, parse them
                pline = pline[pline.find("(") + 1 : pline.find(")")]
                if pline:
                    # Partition args: (<id>, [<delim>], [<*args>])
                    pline = pline.partition(", ")

                    # Isolate _id, stripping quotes
                    _id = pline[0].replace('"', "")

                    # If arguments exist beyond _id
                    pline = pline[2].strip()
                    if pline:
                        # Check for *args or **kwargs
                        if (
                            pline[0] == "{"
                            and pline[-1] == "}"
                            and type(eval(pline)) is dict
                        ):
                            _args = pline
                        else:
                            _args = pline.replace(",", "")

                # Join the elements to form the reformatted command line
                line = " ".join([_cmd, _cls, _id, _args])
            except Exception as mess:
                pass
        return line

    def postcmd(self, stop, line):
        """
        Prints '(hbnb) ' if `sys.__stdin__.isatty()` is False.

        Args:
            self: The instance of the `HBNBCommand` class.
            stop (bool): Indicates whether the command loop should exit.
            line (str): The command line input.

        Returns:
            bool: The `stop` parameter value passed to the method.
        """
        # New variable to store the interactivity status of the standard input
        is_interactive = sys.__stdin__.isatty()

        # Check if the standard input is not interactive
        if not is_interactive:
            print("(hbnb) ", end="")

        return stop

    def do_quit(self, command):
        """
        Method to exit the HBNB console.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            command (str): The command string passed to the method.

        Returns:
            None
        """
        exit()

    def help_quit(self):
        """
        Prints the help documentation for the `quit` command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """
        Handles EOF to exit program.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            arg: The argument passed to the method.

        Returns:
            None
        """
        print()
        exit()

    def help_EOF(self):
        """
        Prints the help documentation for the EOF command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """
        Overrides the emptyline method of CMD.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        pass

    def do_create(self, args):
        """Create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = (
                        arg_splited[1].replace("_", " ").replace('"', '\\"')
                    )
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        else:
            if arg_list[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                new_instance = self.classes[arg_list[0]](**kw)
                new_instance.save()
                print(new_instance.id)

    def help_create(self):
        """
        Help information for the create method.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """
        Method to show an individual object.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            args (str): The arguments passed to the command.

        Returns:
            None
        """
        var1 = "** class name missing **"
        var2 = "** class doesn't exist **"
        var3 = "** instance id missing **"
        var4 = "** no instance found **"

        args = args.split()
        if len(args) < 1:
            print(var1)
            return

        c_name = args[0]
        if c_name not in HBNBCommand.classes:
            print(var2)
            return

        if len(args) < 2:
            print(var3)
            return

        c_id = args[1]
        key = f"{c_name}.{c_id}"
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print(var4)

    def help_show(self):
        """
        Help information for the show command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """
        Destroys a specified object.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            args (str): The arguments passed to the command.

        Returns:
            None
        """
        new = args.partition(" ")
        var1 = "** class name missing **"
        var2 = "** class doesn't exist **"
        var3 = "** instance id missing **"
        var4 = "** no instance found **"

        c_name = new[0]
        c_id = new[2]
        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print(var1)
            return

        if c_name not in HBNBCommand.classes:
            print(var2)
            return

        if not c_id:
            print(var3)
            return

        key = c_name + "." + c_id

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print(var4)

    def help_destroy(self):
        """
        Help information for the destroy command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        str1 = "Destroys an individual instance of a class"
        str2 = "Destroys an individual instance of a class"

        print(str1)
        print(str2)

    def do_all(self, args):
        """
        Shows all objects, or all objects of a class.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            args (str): The arguments passed to the command.

        Returns:
            None
        """
        print_list = []
        var1 = "** class doesn't exist **"

        if args:
            class_name = args.split(" ")[0]  # remove possible trailing args
            if class_name not in HBNBCommand.classes:
                print(var1)
                return
            objects = storage.all(HBNBCommand.classes[class_name])
        else:
            objects = storage.all()

        for k, v in objects.items():
            print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """
        Help information for the all command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        var1 = "Shows all objects, or all of a class"
        var2 = "[Usage]: all <className>\n"

        print(var1)
        print(var2)

    def do_count(self, args):
        """
        Count the current number of class instances.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            args (str): The arguments passed to the command.

        Returns:
            None
        """
        count = 0

        for t, v in storage._FileStorage__objects.items():
            if args == t.split(".")[0]:
                count += 1
        print(count)

    def help_count(self):
        """
        Help information for the count command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        var1 = "Usage: count <class_name>"
        print(var1)

    def do_update(self, args):
        """
        Updates a certain object with new information.

        Parameters:
            self: The instance of the `HBNBCommand` class.
            args (str): The arguments passed to the command.

        Returns:
            None
        """
        c_name = c_id = att_name = att_val = kwargs = ""
        var1 = "** class name missing **"
        var2 = "** class doesn't exist **"
        var3 = "** instance id missing **"
        var4 = "** no instance found **"
        var5 = "** attribute name missing **"
        var6 = "** value missing **"

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print(var1)
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print(var2)
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print(var3)
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print(var4)
            return

        # first determine if kwargs or args
        if "{" in args[2] and "}" in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '"':  # check for quoted arg
                second_quote = args.find('"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1 :]

            args = args.partition(" ")

            # if att_name was not quoted arg
            if not att_name and args[0] != " ":
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '"':
                att_val = args[2][1 : args[2].find('"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(" ")[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if i % 2 == 0:
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print(var5)
                    return
                if not att_val:  # check for att_value
                    print(var6)
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """
        Displays help information for the update command.

        Parameters:
            self: The instance of the `HBNBCommand` class.

        Returns:
            None
        """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

        # Additional help information
        print("Description:")
        print("  It requires the following arguments:")
        print("    - className: The name of the class of the object.")
        print("    - id: The ID of the object.")
        print("    - attName: The name of the attribute to be updated.")
        print("    - attVal: The new value for the attribute.")
        print("  If the attribute does not exist, it will be created.")
        print("  The updated object will be saved to the file.")


if __name__ == "__main__":
    # Create an instance of the HBNBCommand class and start the command loop
    HBNBCommand().cmdloop()
