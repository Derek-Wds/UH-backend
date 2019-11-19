import hashlib
import logging
from flask_restful import Resource
from flask import request, session
from database.database import db
from error.errors import *
from models.doctor import *

def loginDoctorHandler():
    try:
        requestData = request.get_json()
        phone = requestData["phone"].strip()
        plaintextPassword = requestData["password"].strip()
        hashedPassword = hashlib.sha256(
            plaintextPassword.encode("utf-8")).hexdigest()

    except Exception as why:
        logging.info("Request is wrong: " + str(why))
        return INVALID_INPUT

    if phone is None or hashedPassword is None:
        return INVALID_INPUT

    doctor = Person.query.filter_by(phone=phone).first()

    if doctor is None:
        return DOES_NOT_EXIST

    if doctor.password != hashedPassword:
        return INVALID_INPUT

    session['phone number'] = phone
    session['role'] = doctor.role

    return {
        'status': 200,
        'msg': 'Success',
        'role': session['role'],
        'session': session['phone number']
    }, 200