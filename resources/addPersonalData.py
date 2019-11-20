import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db

class AddPersonalData(Resource):
    @login_required
    def get(self):
        return EMPTY

    @login_required
    def post(self):
        role = session['role']
        if role == 'doctor':
            return UNAUTHORIZED
        
        try:
            requestData = request.get_json()
            phone = session['phone number']
            name = requestData['name'].strip()
            email = requestData['email'].strip()
            gender = requestData['gender'].strip()
            age = int(requestData['age'])
            address = requestData['address']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        patient = Person.query.filter_by(phone=phone).first()

        if patient is None:
            return DOES_NOT_EXIST
        
        # update attributes
        patient.name = name
        patient.email = email
        patient.gender = gender
        patient.age = age
        patient.address = address
        db.session.commit()
        
        return {
            'status': 200,
            'msg': 'Success',
            'role': session['role'],
            'session': session['phone number'],
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
