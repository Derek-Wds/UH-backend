import logging
from flask import request, session
from resources import *
from handlers.addLogHandlerFactory import *
from flask_restful import Resource
from config.auth import *
from error.errors import *

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
        t = requestData["type"]
        logHandler = addLogHandlerFactory(t)
        
        return logHandler()

    @login_required
    def put(self):
        return EMPTY

    @login_required
    def delete(self):
        return EMPTY
