import hashlib
import logging
from flask_restful import Resource
from flask import request
from database.database import db
from error.errors import *
from models.doctor import *

def registerDoctorHandler():
    try:
        requestData = request.get_json()
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

    doctor = Person.query.filter_by(phone=phone).first()

    if doctor is not None:
        return ALREADY_EXIST

    doctor = Doctor(username, str(phone), str(hashedPassword))
    db.session.add(doctor)
    db.session.commit()

    return {
        'status': 200,
        'msg': 'Success',
        'username': username
    }, 200