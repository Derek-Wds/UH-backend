import requests, json, pytest
from flask import Flask, request, session
from pytest_regressions import data_regression
from app import *

app = create_app()
app.testing = True
init_routes(app)

global ID
global DID
global DDID
global MID