import logging, hashlib
from flask import request
from resources import *
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models import *

class LoginAuth(Resource):
    def get(self):
        return EMPTY

    def post(self):
        try:
            requestData = request.get_json()
            phone = requestData["phone"].strip()
            plaintextPasword = requestData["password"].strip()
            hashedPassword = hashlib.sha256(
                plaintextPasword.encode("utf-8")).hexdigest()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        if phone is None or hashedPassword is None:
            return INVALID_INPUT
        
        person = Person.query.filter_by(phone=phone).first()

        if person is None:
            return DOES_NOT_EXIST
        
        if person.password != hashedPassword:
            return INVALID_INPUT
        
        session['phone number'] = phone
        session['role'] = person.role

        return {
            'status': 200,
            'msg': 'Success',
            'role': session['role'],
            'session': session['phone number']
        }, 200

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
