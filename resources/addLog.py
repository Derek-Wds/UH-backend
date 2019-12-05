import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from database.database import db
from error.errors import *
from models import *

class AddLog(Resource):
    @login_required
    def get(self):
        return EMPTY

    @login_required
    def post(self):
        role = session['role']
        if role == 'doctor':
            return UNAUTHORIZED
        requestData = request.get_json()
        t = requestData["t"]
        try:
            requestData = request.get_json()
            patient_phone = session['phone number']
            title = requestData['title'].strip()
            content = requestData['content'].strip()
            if t == 'detailed':
                date = requestData['date']
                data = requestData['data']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT

        if patient_phone is None:
            return INVALID_INPUT

        patient = Person.query.filter_by(phone=patient_phone).first()

        if patient is None:
            return DOES_NOT_EXIST
        
        if patient.role != 'patient':
            return INVALID_INPUT

        if t == 'simple':
            log = SimpleLog(patient_phone, title, content)
        else:
            log = DetailedLog(patient_phone, patient_phone, date, title, content, data)
        db.session.add(log)
        db.session.commit()

        session['phone number'] = patient_phone
        session['role'] = patient.role

        return {
            'status': 200,
            'msg': 'Success',
            'log id': log.id,
            'role': session['role'],
            'session': session['phone number']
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
