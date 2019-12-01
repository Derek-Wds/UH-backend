from tests.base import *
from datetime import datetime

# Add personal log
def test_add_log(data_regression):
    data = {
        'phone': '12345678',
        'doctor_phone': '11111111',
        'title': 'Catch a cold',
        'content': 'I drink a lot of water today',
        't': 'simple'}
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'patient'
            session['phone number'] = '12345678'
        resp = c.post('/add/log', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        ID = result['log id']
        data_regression.check(result)

# Add personal detailed log
def test_add_detailed_log(data_regression):
    data = {
        'phone': '12345678',
        'doctor_phone': '11111111',
        'title': 'Catch a cold',
        'content': 'I drink a lot of water today',
        'date': json.dumps(datetime(2020, 5, 17).__str__()),
        'data': {
            'cold': 'have a low fever for a week',
            'cough': 'have a sore throat for two days, and wants to drink water all the time'
        },
        't': 'detailed'}
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'patient'
            session['phone number'] = '12345678'
        resp = c.post('/add/log', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        DID = result['log id']
        data_regression.check(result)