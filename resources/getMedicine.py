import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.medicine import *
from models.person import *

class GetMedicine(Resource):
    @login_required
    def get(self):
        return EMPTY

    @login_required
    def post(self):
        role = session['role']
        try:
            requestData = request.get_json()
            patient_phone = requestData['patient_phone'].strip()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        if role == 'patient' and patient_phone != session['phone number']:
            return UNAUTHORIZED
        
        person = Person.query.filter_by(phone=patient_phone).first()

        if person is None:
            return DOES_NOT_EXIST
        
        # get attributes
        output = list()
        pills = Medicine.query.filter_by(patient_phone=patient_phone).all()
        for pill in pills:
            data = dict()
            data['patient_phone'] = pill.patient_phone
            data['patient_name'] = person.name
            data['name'] = pill.name
            data['description'] = pill.description
            data['times'] = pill.times
            output.append(data)
        
        return {
            'status': 200,
            'msg': 'Success',
            'data': output,
            'role': session['role'],
            'session': session['phone number']
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
