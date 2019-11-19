import logging
from flask import request
from resources import *
from handlers.registerHandlerFactory import *
from flask_restful import Resource

class RegisterAuth(Resource):
    def get(self):
        return EMPTY

    def post(self):
        try:
            requestData = request.get_json()
            role = requestData["role"]
            registerHandler = registerHandlerFactory(role)
            
            return registerHandler()
        except Exception as e:
            return INVALID_INPUT

    def put(self):
        return EMPTY

    def delete(self):
        return EMPTY
