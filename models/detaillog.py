import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

class DetailedLog(Log, Time, Diseases):
    __tablename__ = 'detailed_log'
    __mapper_args__ = {'polymorphic_identity': 'detailed'}
    date = db.Column('date', db.DATE, default = datetime.utcnow) # appointment date

    def __init__(self, phone, patient_name, patient_phone, date, title, content, diseases):
        self.phone_id = phone
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.date = date
        self.title = title
        self.content = content
        self.diseases = diseases
        self.t = 'detailed'

    def __repr__(self):
        return '<Detailed Log File {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}