import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

# db table for diagnosis
class Diagnosis(Log, Time, Diseases):
    __tablename__ = 'diagnosis'
    __mapper_args__ = {'polymorphic_identity': 'diagnosis'}
    doctor_phone = db.Column('doctor_phone', db.String)  

    def __init__(self, patient_phone, doctor_phone, date, title, content, diseases):
        self.patient_phone = patient_phone
        self.doctor_phone = doctor_phone
        self.time = date
        self.title = title
        self.content = content
        self.diseases = diseases
        self.t = 'diagnosis'

    def __repr__(self):
        return '<Diagnosis File {}>'.format(self.title + '_' + self.doctor_phone + '_' + self.patient_phone)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}