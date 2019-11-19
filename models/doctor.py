import json
from database.database import db
from models.base import *
from models.person import *

class Doctor(Person, Name, Email):
    __tablename__ = 'doctor'
    __mapper_args__ = {'polymorphic_identity': 'doctor'}

    def __init__(self, username, phone, password):
        self.username = username
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<Doctor {}>'.format(self.username)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}