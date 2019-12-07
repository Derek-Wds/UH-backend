import logging, time
from flask import request, session
from resources import *
from flask_restful import Resource
from database.database import db
from models import *
from sms.message import *
from datetime import datetime


while True:
    # get all the medicines
    medicines = Medicine.query.all()
    for medicine in medicines:
        # today
        today = datetime.now()

        # get time from db
        times = medicine.times
        start = datetime.strptime(medicine.start_time, '%Y-%m-%d') 
        end = datetime.strptime(medicine.end_time, '%Y-%m-%d')

        # get patient
        patient = Person.query.filter_by(phone=medicine.patient_phone).first()

        if start <= today and end >= today:
            for i, time in times.items():
                t = datetime.strptime(str(today.year) + '-' + str(today.month) + '-' +\
                    str(today.day) + ' ' + str(time), '%Y-%m-%d %I:%M')
                difference = (t - today).total_seconds()
                if difference > 0 and difference < 1800:
                    message = 'please remember to take the medicine {0} at {1}'.format(medicine.name, time)
                    send_message(medicine.patient_phone, patient.name, message, 'Automatic reminder')
                    break
    # break
    time.sleep(1800)