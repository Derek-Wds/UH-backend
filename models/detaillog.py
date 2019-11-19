import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

class DetailedLog(Log, Time, Diseases):
    __tablename__ = 'detailed_log'
    __mapper_args__ = {'polymorphic_identity': 'detailed'}
    app_date = db.Column('appointement_date', db.DATE, nullable = False) # appointment date

    def __init__(self, phone, patient_name, patient_phone, doctor_name, doctor_phone, app_date, title, content, diseases):
        self.phone_id = phone
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.doctor_name = doctor_name
        self.doctor_phone = doctor_phone
        self.app_date = date
        self.time = datetime.utcnow
        self.title = title
        self.content = content
        self.diseases = diseases
        self.t = 'detailed'

    def __repr__(self):
        return '<Detailed Log File {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}