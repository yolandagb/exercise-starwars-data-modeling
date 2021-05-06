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


class Home (Base):
     __tablename__ = 'home'
     id = Column(Integer, primary_key=True)
     password = Column(Integer, ForeignKey('Login.Password'))
     user_name =  Column(Integer, ForeignKey('User.user_name'))
     url = Column(String(250), nullable=False)
     user_id = Column(Integer, ForeignKey('user.id'))
     post = Column(Integer, ForeignKey('post.id'))
     planets_post = Column(Integer, ForeignKey('planets.post'))
     characters_post = Column(Integer, ForeignKey('characters.post'))
     

class User(Base):
     __tablename__ = 'User'
     id = Column(Integer, primary_key=True)
     username = Column(String(250))
     password = Column(Integer, ForeignKey('Login.password'))
     email = Column(String(250), nullable=False)
     post = Column(Integer, ForeignKey('post.id'))

class Like (Base):
     __tablename__ = 'like'
     # Here we define columns for the table address.
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     likes = Column(String(250))
     user_id = Column(Integer, ForeignKey('post.id'))
     like = Column(Integer, ForeignKey('like.id'))
     planets_post = Column(Integer, ForeignKey ('planets.post'))
     characters_post = Column(Integer, ForeignKey('characters.post'))
     
# class Characters (Base):
#     __tablename__ = 'characters'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     likes = Column(String(250))
#     user_id = Column(Integer, ForeignKey('user.id'))
#     like = Column(Integer, ForeignKey('like.id'))
#     login = relationship('Login')
#     user = relationship ('User')    


#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
