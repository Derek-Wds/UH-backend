import hashlib
import logging
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models.detaillog import *
from models.person import *

def addDetailLogHandler():
    try:
        requestData = request.get_json()
        patient_phone = session['phone number']
        title = requestData['title'].strip()
        content = requestData['content'].strip()
        date = requestData['date']
        data = requestData['data']
        t = 'detailed'

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

    patient_name = patient.name

    dlog = DetailedLog(patient_phone, patient_name, patient_phone, date, title, content, data)
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