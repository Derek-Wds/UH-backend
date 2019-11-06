import os
import sys
import hashlib
from flask import Flask, request, session, send_file, jsonify, send_from_directory
from flask_cors import CORS
from database.database import db
from config import *


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.abspath('app.cfg'))

    # Database initialize with app
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    return app


# api.add_resource()
if __name__ == "__main__":
    app = create_app()
    CORS(app, supports_credentials=True)
    init_routes(app)

    app.run(port=5000, debug=True, host='0.0.0.0', use_reloader=True)
