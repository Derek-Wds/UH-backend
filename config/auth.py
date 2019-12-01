from flask_httpauth import HTTPTokenAuth
from functools import wraps
from flask import session
from error.errors import *

auth = HTTPTokenAuth('Protection')

# required login
def login_required(f):
    @wraps(f)
    def dec(*args, **kwargs):
        if not "phone number" in session:
            return UNAUTHORIZED
        return f(*args, **kwargs)
    return dec