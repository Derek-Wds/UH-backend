import os
import json
from database.database import db
from models.base import *


class Person(db.Model):
    __tablename__ = 'person'
    usrname = db.Column('usrname', db.String, nullable=False)
    phone = db.Column('phone', db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)
    role = db.Column('role', db.String, nullable=False)
    __mapper_args__ = {'polymorphic_on': role}

    def __init__(self, usrname, phone, password, role):
        self.usrname = usrname
        self.phone = phone
        self.password = password
        self.role = role

    def __repr__(self):
        return '<Person {}>'.format(self.name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
