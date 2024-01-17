#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State.

    Attributes:
        name (str): The name of the state.
        cities (relationship): A one-to-many relationship with City objects.
    """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """Retrieve the cities associated with the current state.

        Returns:
            list: A list of City objects associated with the state.
        """
        try:
            all_objects = models.storage.all()
            city_objects = []
            result = []
            city_type = "City"

            # Filter out objects that represent cities
            for key in all_objects:
                object_type = key.replace(".", " ")
                object_type = shlex.split(object_type)
                if object_type[0] == city_type:
                    city_objects.append(all_objects[key])

            # Find cities that belong to the current state
            for city in city_objects:
                if city.state_id == self.id:
                    result.append(city)

            return result
        except Exception as e:
            print(f"An error occurred: {e}")
