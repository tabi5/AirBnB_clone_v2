#!/usr/bin/python3

"""
DESCRIPTION:
    This script defines the FileStorage class for AirBnB, which
    serializes instances to a JSON file and deserializes JSON
    files to instances.

MODULES:
    - json: Provides methods for working with JSON data.
    - models.base_model: Importing the BaseModel class.
    - models.user: Importing the User class.
    - models.state: Importing the State class.
    - models.city: Importing the City class.
    - models.amenity: Importing the Amenity class.
    - models.place: Importing the Place class.
    - models.review: Importing the Review class.
    - shlex: Provides a lexical analyzer for simple syntaxes.

CLASSES:
    - FileStorage: A class that handles serialization and
      deserialization of instances to/from a JSON file.

ATTRIBUTES:
    - __file_path: The path to the JSON file.
    - __objects: A dictionary that stores the serialized objects.

METHODS:
    - all(self, cls=None): Returns a dictionary of objects.
    - new(self, obj): Sets the __objects dictionary.
    - save(self): Serializes the objects to the JSON file.
    - reload(self): Deserializes the JSON file to objects.
    - delete(self, obj=None): Deletes an object from __objects.
    - close(self): Calls the reload() method.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """
    DESCRIPTION:
        This class serializes instances to a JSON file and
        deserializes JSON file to instances.

    ATTRIBUTES:
        - __file_path: path to the JSON file
        - __objects: objects will be stored
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        DESCRIPTION:
            Returns a dictionary of objects.

        PARAMETERS:
            - cls: The class type to filter the objects (optional).

        RETURN:
            A dictionary of objects filtered by cls if provided, or
            all objects if cls is None.
        """
        try:
            new_dictionary = {}
            if cls:
                object_dictionary = self.__objects
                for key in object_dictionary:
                    partition = key.replace('.', ' ')
                    partition = shlex.split(partition)
                    if partition[0] == cls.__name__:
                        new_dictionary[key] = self.__objects[key]
                return new_dictionary
            else:
                return self.__objects
        except Exception as ex:
            raise Exception("An error occurred in the 'all' method: " +
                            str(ex))

    def new(self, obj):
        """
        DESCRIPTION:
            Sets the __objects dictionary.

        PARAMETERS:
            - obj: The object to be set in the __objects dictionary.
        """
        try:
            if obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                self.__objects[key] = obj
        except Exception as ex:
            raise Exception("An error occurred in the 'new' method: " +
                            str(ex))

    def save(self):
        """
        DESCRIPTION:
            Serializes the objects to the JSON file.
        """
        try:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(my_dict, f)
        except Exception as e:
            raise Exception("An error occurred in the 'save' method: " +
                            str(e))

    def reload(self):
        """
        DESCRIPTION:
            Deserializes the JSON file to objects.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
        except Exception as ex:
            raise Exception("An error occurred in the 'reload' method: " +
                            str(ex))

    def delete(self, obj=None):
        """
        DESCRIPTION:
            Deletes an object from __objects.

        PARAMETERS:
            - obj: The object to be deleted from __objects.
        """
        try:
            if obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
        except Exception as e:
            raise Exception("An error occurred in the 'delete' method: "
                            + str(e))

    def close(self):
        """
        DESCRIPTION:
            Calls the reload() method.
        """
        try:
            self.reload()
        except Exception as e:
            raise Exception("An error occurred in the 'close' method: " +
                            str(e))
