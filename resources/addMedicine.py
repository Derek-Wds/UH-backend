import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.medicine import *
from models.patient import *

class AddMedicine(Resource):
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
            patient_phone = requestData['patient_phone'].strip()
            name = requestData['name'].strip()
            description = requestData['description'].strip()
            times = requestData['times']
            start_time = requestData['start_time']
            end_time = requestData['end_time']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        if end_time < start_time:
            return INVALID_INPUT

        person = Patient.query.filter_by(phone=patient_phone).first()

        if person.role != 'patient':
            return INVALID_INPUT

        if person is None:
            return DOES_NOT_EXIST
        
        # update attributes
        medicine = Medicine(patient_phone, name, description, times, start_time, end_time)
        db.session.add(medicine)
        db.session.commit()
        
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
