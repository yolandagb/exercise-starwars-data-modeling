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
     __tablename__ = 'User'
     id = Column(Integer, primary_key=True)
     username = Column(String(250))
     nickname =  Column(Integer, ForeignKey('User.user_name'))
     email = Column(String(250), nullable=False)
     password = Column(Integer, ForeignKey('Login.password'))
     Favorites = Column(Integer, ForeignKey('favorites.id'))

class Favorites (Base):
     __tablename__ = 'favorites'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('post.id'))
     favorites = Column(String(250))
    #  like = Column(Integer, ForeignKey('like.id'))
     planets = Column(Integer, ForeignKey ('planets.post'))
     characters = Column(Integer, ForeignKey('characters.post'))
     
     
class Characters (Base):
     __tablename__ = 'characters'
     # Here we define columns for the table address.
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     User_id = Column(Integer, ForeignKey('user.id')) 
     Favorites = Column(String(250))
     Comment = Column(String(250)) 

class Planets (Base):
     __tablename__ = 'planets'
     # Here we define columns for the table address.
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     Favorites = Column(String(250))
     User_id = Column(Integer, ForeignKey('user.id')) 
     Comment = Column(String(250))      


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
