import os
import json
from database.database import db
from models.base import *

# db table for person
class Person(db.Model):
    __tablename__ = 'person'
    username = db.Column('username', db.String, nullable=False)
    phone = db.Column('phone', db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)
    role = db.Column('role', db.String, nullable=False)
    gender = db.Column('gender', db.String, default = '')
    age = db.Column('age', db.Integer, default = -1)
    address = db.Column('address', db.String, default = '')
    image = db.Column('image', db.String, default = '')
    __mapper_args__ = {'polymorphic_on': role}

    def __init__(self, username, phone, password, role):
        self.username = username
        self.phone = phone
        self.password = password
        self.role = role

    def __repr__(self):
        return '<Person {}>'.format(self.username)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Name(object):
    @declared_attr
    def name(cls):
        return cls.__table__.c.get('name', db.Column(db.String, default = ''))

class Email(object):
    @declared_attr
    def email(cls):
        return cls.__table__.c.get('email', db.Column(db.String, default = ''))
