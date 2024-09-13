import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    email = Column(String(250), primary_key = True)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer,ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text =  Column(String(250), nullable = False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Column(Enum('image', 'video', 'audio', name='media_types'), nullable=False)
    url = Column(String(250), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

