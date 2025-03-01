from tests.base import *

# Get doctor personal data
def test_get_doctor_data(data_regression):
    data = {
         'phone': '11111111'
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'doctor'
            session['phone number'] = '11111111'
        resp = c.post('/get/data', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)


# Get patient personal data
def test_get_patient_data(data_regression):
    data = {
         'phone': '12345678'
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'patient'
            session['phone number'] = '12345678'
        resp = c.post('/get/data', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)