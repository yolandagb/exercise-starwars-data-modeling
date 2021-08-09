import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)




class User(Base):
     __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    first_name =Column(String(80), nullable=False)
    last_name =Column(String(80), nullable=False)
    created_at =Column(String(80))
    updated_at =Column(String(80))
    email =Column(String(80),unique=True, nullable=False) 
    
    # RELATIONSHIP
     favourites = relationship('Favourite', backref="user", lazy=True)
     characters = relationship('Character', backref="user", lazy=True)
     planets = relationship('Planet', backref="user", lazy=True)


class Favourite (Base):
     __tablename__ = 'favourites'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    fav_planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    fav_character_id = Column(Integer, ForeignKey('character.character_id'))
     
     
class Characters (Base):
     __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name =  Column(String(200))
    birth_year = Column(Integer)
    gender = Column(String(200))
    height = Column(Integer)
    skin_color = Column(String(200))
    eye_color = Column(String(200))
     

class Planets (Base):
     __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    climate = Column(String(200))
    population = Column(Integer)
    orbital_period = Column(Integer)
    diameter= Column(Integer)


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
