import json
from database.database import db
from models.base import *
from models.person import *

class Patient(Person):
    __tablename__ = 'patient'
    __mapper_args__ = {'polymorphic_identity': 'patient'}
    name = db.Column('name', db.String, default = '')
    email = db.Column('email', db.String, default = '')
    gender = db.Column('gender', db.String, default = '')
    age = db.Column('age', db.Integer, default = -1)
    address = db.Column('address', db.String, default = ''

    def __init__(self, username, phone, password):
        self.username = username
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<Patient {}>'.format(self.username)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}