import logging, hashlib
from flask import request
from resources import *
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models.person import *

# handler for register
class RegisterAuth(Resource):
    def get(self):
        return EMPTY

    def post(self):
        try:
            requestData = request.get_json()
            role = requestData["role"]
            username = requestData["username"]
            phone = requestData["phone"]
            plaintextPasword = requestData["password"]
            hashedPassword = hashlib.sha256(
                plaintextPasword.encode("utf-8")).hexdigest()

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        if username is None or hashedPassword is None or phone is None:
            return INVALID_INPUT
            
        person = Person.query.filter_by(phone=phone).first()

        if person is not None:
            return ALREADY_EXIST

        person = Person(username, str(phone), str(hashedPassword), role)
        db.session.add(person)
        db.session.commit()

        return {
            'status': 200,
            'msg': 'Success',
            'username': username
        }, 200

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
