#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """This is the class for Place.

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

    vartname = "places"
    __tablename__ = vartname
    varcitiesid = "cities.id"
    varusersid = "users.id"
    varAmenity = "Amenity"
    varplace_amenities = "place_amenities"

    varReview = Review
    city_id = Column(String(60), ForeignKey(varcitiesid), nullable=False)
    user_id = Column(String(60), ForeignKey(varusersid), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            varReview, cascade="all, delete, delete-orphan", backref="place"
        )
        amenities = relationship(
            varAmenity,
            secondary=place_amenity,
            viewonly=False,
            back_populates=varplace_amenities,
        )
    else:
        # Code for file storage
        @property
        def reviews(self):
            """Returns list of reviews.id"""
            all_objects = models.storage.all()
            review_objects = []
            result = []
            for key in all_objects:
                split_key = key.replace(".", " ")
                split_key = shlex.split(split_key)
                if split_key[0] == "Review":
                    review_objects.append(all_objects[key])
            for review in review_objects:
                if review.place_id == self.id:
                    result.append(review)
            return result
        def reviews(self):
            """
            Returns a list of reviews from reviews.id.

            Returns:
                - result (list): List of review objects associated with the current object.

            Exceptions:
                - Exception: If an error occurs during the retrieval of reviews.
            """
            try:
                var = models.storage.all()
                lista = []
                result = []
                for key in var:
                    review = key.replace('.', ' ')
                    review = shlex.split(review)
                    if review[0] == 'Review':
                        lista.append(var[key])
                for elem in lista:
                    if elem.place_id == self.id:
                        result.append(elem)
                return result
            except Exception as e:
                print(f"An error occurred: {e}")

        @property
        def amenities(self):
            """Returns a list of amenity IDs associated with the instance."""
            try:
                return self.amenity_ids
            except Exception as e:
                print(f"An error occurred: {e}")

        @amenities.setter
        def amenities(self, obj=None):
            """
            Appends amenity ids to the attribute.

            Description:
                Appends the id of an Amenity object to the amenity_ids attribute.

            Parameters:
                - obj (Amenity, optional): An instance of the Amenity class.

            Exceptions:
                - TypeError: If obj is not an instance of the Amenity class or if obj is None.
                - AttributeError: If obj does not have an 'id' attribute.
            """
         
            try:
                is_obj_amenity = type(obj) is Amenity
                is_obj_id_not_in_amenity_ids = obj.id not in self.amenity_ids

                if is_obj_amenity and is_obj_id_not_in_amenity_ids:
                    self.amenity_ids.append(obj.id)
            except Exception as e:
                print(f"An error occurred: {e}")
