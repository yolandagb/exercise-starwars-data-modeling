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
     nickname = Column(String(250))
     email = Column(String(250), nullable=False)
     password = Column(String(120))
     favorites_post = Column(Integer, ForeignKey('favorites.id'))

class Favorites (Base):
     __tablename__ = 'favorites'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     planets_post= Column(Integer, ForeignKey ('planets.id'))
     characters_post = Column(Integer, ForeignKey('characters.id'))
     
     
class Characters (Base):
     __tablename__ = 'characters'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id')) 
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
