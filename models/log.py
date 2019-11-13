import os
import json
from database.database import db
from models.base import *

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column('id', db.Integer, primary_key = True, unique = True, nullable = False)
    patient_phone = db.Column(db.String, db.ForeignKey('patient.phone'), nullable = False)
    doctor_phone = db.Column(db.String, db.ForeignKey('doctor.phone'), nullable = False)
    patient_name = db.Column('patient_name', db.String, nullable = False)
    doctor_name = db.Column('doctor_name', db.String, nullable = False)
    title = db.Column('title', db.String, nullable = False)
    content = db.Column('content', db.String, nullable = False)
    t = db.Column('type', db.String, nullable = False)
    __mapper_args__ = {'polymorphic_on': t}

    def __init__(self, patient_phone, doctor_phone, patient_name, doctor_name, title, content, t):
        self.patient_phone = patient_phone
        self.doctor_phone = doctor_phone
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.title = title
        self.content = content
        self.t = t

    def __repr__(self):
        return '<Log File {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
