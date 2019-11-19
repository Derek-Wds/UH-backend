import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.person import *

class GetPersonalData(Resource):
    @auth.login_required
    def get(self):       
        try:
            requestData = request.get_json()
            patient_phone = requestData['phone']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        role = session['role'] 
        if role == 'patient':
            if patient_phone != session['phone number']:
                return UNAUTHORIZED
        
        patient = Person.query.filter_by(phone=patient_phone).first()

        if patient is None:
            return DOES_NOT_EXIST
        
        # get attributes
        data = dict()
        data['name'] = patient.name
        data['email'] = patient.email
        data['gender'] = patient.gender
        data['age'] = patient.age
        data['address'] = patient.address
        
        return {
            'status': 200,
            'msg': 'Success',
            'data': data,
            'role': session['role'],
            'session': session['phone number'],
        }, 200

    @auth.login_required
    def post(self):
        return EMPTY

    @auth.login_required
    def put(self):
        return EMPTY

    @auth.login_required
    def delete(self):
        return EMPTY
