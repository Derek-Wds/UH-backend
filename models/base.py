import sys, os
sys.path.insert(0, os.path.abspath('..'))
import json
from flask import Flask, request, render_template, jsonify
from sqlalchemy.ext import mutable
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref
from app import db

# class for parse json file into db
class JsonEncodedDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

mutable.MutableDict.associate_with(JsonEncodedDict)