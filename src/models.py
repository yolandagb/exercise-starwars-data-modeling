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


# class Home (Base):
#      __tablename__ = 'home'
#      id = Column(Integer, primary_key=True)
#     #  nickname =  Column(Integer, ForeignKey('User.user_name'))
#     #  user_id = Column(Integer, ForeignKey('user.id'))
#     #  post = Column(Integer, ForeignKey('post.id'))
#      planets_post = Column(Integer, ForeignKey('planets.post'))
#      characters_post = Column(Integer, ForeignKey('characters.post'))
#      password = Column(Integer, ForeignKey('Login.Password'))
#     #  url = Column(String(250), nullable=False)

class User(Base):
     __tablename__ = 'user'
     id = db.Column(db.Integer, primary_key=True)
     nickname = db.Column(db.String(120), nullable=False)
     gender = db.Column(db.Enum(Gender), unique=False, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
     password = Column(String(120))
     image = db.Column(db.String(120), unique=False, nullable=True)
    
    # RELATIONSHIP
     favourites = db.relationship('Favourite', backref="user", lazy=True)
     characters = db.relationship('Character', backref="user", lazy=True)
     planets = db.relationship('Planet', backref="user", lazy=True)


class Favourite (Base):
     __tablename__ = 'favourites'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     favourite_planets= Column(Integer, ForeignKey ('planets.id'))
     favourite_characters = Column(Integer, ForeignKey('characters.id'))
     
     
class Characters (Base):
     __tablename__ = 'characters'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     image = db.Column(db.String, unique=False, nullable=False)
     name = db.Column(db.String(120), unique=False, nullable=False) 
     favorites_list = Column(Integer, ForeignKey('favorites.id'))
     comments = Column(String(500)) 

class Planets (Base):
     __tablename__ = 'planets'
     id = Column(Integer, primary_key=True)
     favorites_list = Column(Integer, ForeignKey('favorites.id'))
     user_id = Column(Integer, ForeignKey('user.id')) 
     comment = Column(String(500))      


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
