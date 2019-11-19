import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from sms.message import *

class AddReminder(Resource):
    @login_required
    def get(self):
        return EMPTY

    @login_required
    def post(self):
        role = session['role']
        if role == 'patient':
            return UNAUTHORIZED
        
        try:
            requestData = request.get_json()
            patient_phone = requestData['phone'].strip()
            message = requestData['message'].strip()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        patient = Person.query.filter_by(phone=phone).first()
        doctor = Person.query.filter_by(phone=session['phone number']).first()

        if patient is None:
            return DOES_NOT_EXIST
        
        if doctor is None:
            return UNAUTHORIZED
        
        # update attributes
        name = patient.name
        d_name = doctor.name
        if not patient_phone.startswith('+86'):
            patient_phone = '+86' + patient_phone
        
        send_message(patient_phone, name, message, d_name)
        
        return {
            'status': 200,
            'msg': 'Success',
            'role': session['role'],
            'session': session['phone number']
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
