import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.diagnosis import *
from models.person import *

class GetDiagnosis(Resource):
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
        if role == 'patient':
            if phone != session['phone number']:
                return UNAUTHORIZED
        
        person = Person.query.filter_by(phone=phone).first()

        if person is None:
            return DOES_NOT_EXIST

        if person.role != 'patient':
            return INVALID_INPUT
        
        # get log
        output = list()
        logs = Diagnosis.query.filter_by(patient_phone=phone).all()
        for log in logs:
            doctor = Person.query.filter_by(phone=log.doctor_phone).first()
            data = dict()
            data['phone'] = log.patient_phone
            data['name'] = person.name
            data['doctor_phone'] = log.doctor_phone
            data['doctor_name'] = doctor.name
            data['title'] = log.title
            data['content'] = log.content
            data['date'] = str(log.time)
            data['data'] = log.diseases
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
