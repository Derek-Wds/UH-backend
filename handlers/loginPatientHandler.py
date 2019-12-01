import hashlib
import logging
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models.patient import *

def loginPatientHandler():
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

    patient = Patient.query.filter_by(phone=phone).first()

    if patient is None:
        return DOES_NOT_EXIST
    
    if patient.password != hashedPassword:
        return INVALID_INPUT
    
    session['phone number'] = phone
    session['role'] = patient.role

    return {
        'status': 200,
        'msg': 'Success',
        'role': session['role'],
        'session': session['phone number']
    }, 200