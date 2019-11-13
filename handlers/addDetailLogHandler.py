import hashlib
import logging
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models.detaillog import *

def addDetailLogHandler():
    try:
        requestData = request.get_json()
        patient_phone = requestData["phone"].strip()
        doctor_phone = requestData['doctor_phone'].strip()
        title = requestData['title'].strip()
        content = requestData['content'].strip()
        app_date = requestData['app_date']
        diseases = requestData['diseases']
        t = 'detailed'

    except Exception as why:
        logging.info("Request is wrong: " + str(why))
        return INVALID_INPUT

    if phone is None:
        return INVALID_INPUT

    patient = Person.query.filter_by(phone=patient_phone).first()
    doctor = Person.query.filter_by(phone=doctor_phone).first()

    if patient is None or doctor is None:
        return DOES_NOT_EXIST
    
    if patient.role != 'patient' or doctor.role != 'doctor':
        return INVALID_INPUT

    patient_name = patient.name
    doctor_name = doctor.name

    dlog = DetailedLog(patient_phone, patient_name, patient_phone, doctor_name, doctor_phone, \
        app_date, title, content, diseases)
    db.session.add(dlog)
    db.session.commit()

    session['phone number'] = patient_phone
    session['role'] = patient.role

    return {
        'status': 200,
        'msg': 'Success',
        'log id': dlog.id,
        'role': session['role'],
        'session': session['phone number']
    }, 200