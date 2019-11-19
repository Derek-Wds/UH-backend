import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

class Diagnosis(Log, Time, Diseases):
    __tablename__ = 'diagnosis'
    __mapper_args__ = {'polymorphic_identity': 'diagnosis'}

    def __init__(self, phone, patient_name, patient_phone, doctor_name, doctor_phone, title, content, diseases):
        self.phone_id = phone
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.doctor_name = doctor_name
        self.doctor_phone = doctor_phone
        self.time = datetime.utcnow
        self.title = title
        self.content = content
        self.diseases = diseases
        self.t = 'diagnosis'

    def __repr__(self):
        return '<Diagnosis File {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}