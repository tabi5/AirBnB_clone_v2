#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """

    __tablename__ = "reviews"
    varplacesid = "places.id"
    varusersid = "users.id"

    try:
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(varplacesid), nullable=False)
        user_id = Column(String(60), ForeignKey(varusersid), nullable=False)
    except Exception as e:
        print(f"An error occurred: {e}")
