import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.person import *

class SearchPatient(Resource):
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
            phone = requestData['phone'].strip()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        person = Person.query.filter_by(phone=phone).first()

        if person is None:
            return DOES_NOT_EXIST
        
        # get attributes
        data = dict()
        data['name'] = person.name
        data['email'] = person.email
        data['gender'] = person.gender
        data['age'] = person.age
        data['address'] = person.address
        
        return {
            'status': 200,
            'msg': 'Success',
            'data': data,
            'role': session['role'],
            'session': session['phone number']
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
