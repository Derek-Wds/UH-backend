import json
from database.database import db
from models.base import *
from models.log import *
from datetime import datetime

class SimpleLog(Log, Time):
    __tablename__ = 'simple_log'
    __mapper_args__ = {'polymorphic_identity': 'simple'}

    def __init__(self, patient_phone, title, content):
        self.patient_phone = patient_phone
        self.title = title
        self.content = content
        self.t = 'simple'

    def __repr__(self):
        return '<Simple Log File {}>'.format(self.title + '_' + self.doctor_name + '_' + self.patient_name)

    @property
    def profile(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
