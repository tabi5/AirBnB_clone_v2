#!/usr/bin/python3
"""This is the Amenity class"""

# Import necessary modules and classes
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    # Define the table name for the class in the database
    __tablename__ = "amenities"

    # Define the columns of the table
    name = Column(String(128), nullable=False)

    # Define the relationship with the Place class through
    # the place_amenity association table
    place_amenities = relationship("Place", secondary=place_amenity)
