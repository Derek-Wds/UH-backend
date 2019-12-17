import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

# db table for detailed log
class DetailedLog(Log, Time, Diseases):
    __tablename__ = 'detailed_log'
    __mapper_args__ = {'polymorphic_identity': 'detailed'}

    def __init__(self, patient_phone, date, title, content, diseases):
        self.patient_phone = patient_phone
        self.time = date
        self.title = title
        self.content = content
        self.diseases = diseases
        self.t = 'detailed'

    def __repr__(self):
        return '<Detailed Log File {}>'.format(self.title + '_' + self.patient_phone)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}