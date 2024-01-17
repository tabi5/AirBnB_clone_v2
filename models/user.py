#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the class for user.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for the user's login.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): A one-to-many relationship with Place objects.
        reviews (relationship): A one-to-many relationship with Review objects.
    """

    __tablename__ = "users"
    VarReview = "Review"
    VarPlace = "Review"
    varuser = "user"

    try:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship(VarPlace, cascade="all, delete, delete-orphan",
                              backref=varuser)
        reviews = relationship(VarReview, cascade="all, delete, delete-orphan",
                               backref=varuser)
    except Exception as e:
        print(f"An error occurred: {e}")
