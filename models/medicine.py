import os
import json
from database.database import db
from models.base import *
from datetime import datetime

class Medicine(db.Model):
    __tablename__ = 'log'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    patient_phone = db.Column('patient_phone', db.String, nullable = False)
    patient_name = db.Column('patient_name', db.String, nullable = False)
    name = db.Column('name', db.String, nullable = False)
    description = db.Column('description', db.String, nullable = False)
    times = db.Column('times', JsonEncodedDict, nullable=False)

    def __init__(self, patient_phone, patient_name, name, description, times):
        self.patient_phone = patient_phone
        self.patient_name = patient_name
        self.name = name
        self.description = description
        self.times = times

    def __repr__(self):
        return '<Medicine {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}