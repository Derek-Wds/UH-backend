import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.person import *

class GetPersonalData(Resource):
    @login_required
    def get(self):       
        return EMPTY

    @login_required
    def post(self):
        try:
            requestData = request.get_json()
            phone = requestData['phone']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        role = session['role']
        if phone != session['phone number']:
            return UNAUTHORIZED
        
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
            'session': session['phone number'],
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
