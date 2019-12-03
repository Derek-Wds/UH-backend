import logging
from flask import request, session
from resources import *
from flask_restful import Resource
from config.auth import *
from error.errors import *
from database.database import db
from models.person import *
from models.diagnosis import *

class AddDiagnosis(Resource):
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
            patient_phone = requestData['phone'].strip()
            doctor_phone = requestData['doctor_phone'].strip()
            date = requestData['date']
            title = requestData['title'].strip()
            content = requestData['content'].strip()
            diseases = requestData['diseases']

        except Exception as why:
            logging.info("Request is wrong: " + str(why))
            return INVALID_INPUT
        
        patient = Person.query.filter_by(phone=patient_phone).first()
        doctor = Person.query.filter_by(phone=doctor_phone).first()

        if patient is None or doctor is None:
            return DOES_NOT_EXIST
        
        if patient.role != 'patient' or doctor.role != 'doctor':
            return INVALID_INPUT
        
        patient_name = patient.name
        doctor_name = doctor.name

        diagnosis = Diagnosis(patient_phone, patient_name, patient_phone, doctor_name, doctor_phone,\
             date, title, content, diseases)
        db.session.add(diagnosis)
        db.session.commit()

        session['phone number'] = doctor_phone
        session['role'] = doctor.role
        
        return {
            'status': 200,
            'msg': 'Success',
            'diagnosis id': diagnosis.id,
            'role': session['role'],
            'session': session['phone number']
        }, 200

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
