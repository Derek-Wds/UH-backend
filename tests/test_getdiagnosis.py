from tests.base import *
from datetime import datetime

# Get personal diagnosis
def test_get_diagnosis(data_regression):
    data = {
        'phone': '12345678'}
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'patient'
            session['phone number'] = '12345678'
        resp = c.post('/get/diagnosis', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)