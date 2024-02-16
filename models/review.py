#!/usr/bin/python3
"""This is the review class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """This is a class for Review
    Attributes:
       city_id (str): The ID of the city associated with the place.
       user_id (str): The ID of the user associated with the place.
       name (str): The name of the place.
       description (str): The description of the place.
       number_rooms (int): The number of rooms in the place.
       number_bathrooms (int): The number of bathrooms in the place.
       max_guest (int): The maximum number of guests allowed in the place.
       price_by_night (int): The price per night for staying in the place.
       latitude (float): The latitude coordinate of the place.
       longitude (float): The longitude coordinate of the place.
       amenity_ids (list): A list of Amenity IDs associated with the place.
       reviews (relationship): A relationship to the Review model,
       representing the reviews of the place.
       amenities (relationship): A relationship to the Amenity model,
       representing the amenities of the place.

    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    # Change the name of the property to avoid conflicts
    # reviewer = relationship("User", backref="reviews")
