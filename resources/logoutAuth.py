import logging
from flask import request, session
from flask_restful import Resource
from resources import *
from handlers.loginHandlerFactory import *
from error.errors import *
from config.auth import *

class LogoutAuth(Resource):
    @auth.login_required
    def get(self):
        return EMPTY

    @auth.login_required
    def post(self):
        if 'phone number ' in session:
            session.pop('phone number', None)
            session.pop('role', None)
        else:
            return UNAUTHORIZED
        
        return {
            'status': 200,
            'msg': 'You have been successfully logged out.'
        }, 200

    @auth.login_required
    def put(self):
        return EMPTY

    @auth.login_required
    def delete(self):
        return EMPTY