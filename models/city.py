#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    __tablename__ = "City"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    places = relationship("Place", backref="cities", cascade="delete")

    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
