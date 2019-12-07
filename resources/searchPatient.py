import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models import *

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
            name = requestData['name'].strip()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        people = Patient.query.filter(Patient.name.like('%{}%'.format(name))).all()

        if people is None:
            return DOES_NOT_EXIST
        
        # get all matched people
        output = list()
        for person in people:
            data = dict()
            data['name'] = person.name
            data['phone'] = person.phone
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
