#!/usr/bin/python3
"""This is the BaseModel class for AirBnB"""

# Import necessary modules and classes
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

# Create a base class for declarative models
Base = declarative_base()


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    # Define the 'id' attribute/column
    id = Column(String(60), unique=True, nullable=False, primary_key=True)

    # Define the 'created_at' attribute/column
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    # Define the 'updated_at' attribute/column
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of the base model class

        Args:
            args: positional arguments (not used in this implementation)
            kwargs: keyword arguments for the constructor of the BaseModel

        Attributes:
            id: A unique ID generated for the instance
            created_at: The date and time of creation
            updated_at: The date and time of the last update
        """
        varcreated_at = "created_at"
        varupdated_at = "updated_at"

        if kwargs:
            # If keyword arguments are provided
            for key, value in kwargs.items():
                if key == varcreated_at or key == varupdated_at:
                    # If the key is "created_at" or "updated_at",
                    # parse the value as a datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # Set the attribute with the key to the corresponding value
                    setattr(self, key, value)

            if "id" not in kwargs:
                # If "id" is not provided as a keyword argument,
                # generate a unique ID using uuid.uuid4()
                self.id = str(uuid.uuid4())

            if varcreated_at not in kwargs:
                # If "created_at" is not provided as a keyword argument,
                # set it to the current datetime using datetime.now()
                self.created_at = datetime.now()

            if varupdated_at not in kwargs:
                # If "updated_at" is not provided as a keyword argument,
                # set it to the current datetime using datetime.now()
                self.updated_at = datetime.now()
        else:
            # If no keyword arguments are provided
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = (
                self.updated_at
            ) = (
                datetime.now()
            )  # Set the creation and update datetime to the current datetime

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string containing the class name, id, and
            dictionary representation of the object.
        """
        class_name = type(self).__name__
        id = self.id
        dict_repr = self.__dict__

        return "[{}] ({}) {}".format(class_name, id, dict_repr)

    def __repr__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string containing the class name, id,
            and dictionary representation of the object.
        """
        return self.__str__()

    def save(self):
        """
        Update the public instance attribute `updated_at`
        to the current date and time.
        Add the object to the data storage and save the changes.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Create a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all the key-value pairs
            in the object's __dict__ attribute.
        """
        # New variables
        class_name = str(type(self).__name__)
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        my_dict = dict(self.__dict__)
        my_dict["__class__"] = class_name
        my_dict["created_at"] = created_at_iso
        my_dict["updated_at"] = updated_at_iso
        if "_sa_instance_state" in my_dict.keys():
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """
        Delete the object from the data storage.

        Returns:
            None
        """
        models.storage.delete(self)
