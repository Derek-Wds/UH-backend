import os
import json
from database.database import db
from models.base import *
from datetime import datetime

# db table for medicine
class Medicine(db.Model):
    __tablename__ = 'medicine'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    patient_phone = db.Column('patient_phone', db.String, nullable = False)
    name = db.Column('name', db.String, nullable = False)
    description = db.Column('description', db.String, nullable = False)
    times = db.Column('times', JsonEncodedDict, nullable=False)
    start_time = db.Column('start_time', db.Date, nullable = False)
    end_time = db.Column('end_time', db.Date, nullable = False)

    def __init__(self, patient_phone, name, description, times, start_time, end_time):
        self.patient_phone = patient_phone
        self.name = name
        self.description = description
        self.times = times
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '<Medicine {}>'.format(self.name + '_' + self.patient_phone)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}