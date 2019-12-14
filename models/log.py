import os
import json
from database.database import db
from models.base import *
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    patient_phone = db.Column('patient_phone', db.String, nullable = False)
    title = db.Column('title', db.String, nullable = False)
    content = db.Column('content', db.String, nullable = False)
    t = db.Column('type', db.String, nullable = False)
    __mapper_args__ = {'polymorphic_on': t}

    def __init__(self, patient_phone, title, content, t):
        self.patient_phone = patient_phone
        self.title = title
        self.content = content
        self.t = t

    def __repr__(self):
        return '<Log File {}>'.format(self.title + '_' + self.patient_phone)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Time(object):
    @declared_attr
    def time(cls):
        return cls.__table__.c.get('time', db.Column(db.TIMESTAMP, default = datetime.utcnow))

class Diseases(object):
    @declared_attr
    def diseases(cls):
        return cls.__table__.c.get('diseases', db.Column(JsonEncodedDict))
