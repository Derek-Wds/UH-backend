from tests.base import *

# Add doctor personal data
def test_add_doctor_data(data_regression):
    data = {
        'name': 'Liu Cixin',
        'email': 'test@test.com',
        'gender': 'male',
        'age': 35,
        'address': 'Century Avenue No.1555'
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'doctor'
            session['phone number'] = '11111111'
        resp = c.post('/add/data', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)


# Add patient personal data
def test_add_patient_data(data_regression):
    data = {
        'name': 'Han Han',
        'email': 'test2@test.com',
        'gender': 'male',
        'age': 22,
        'address': 'Century Avenue No.1555'
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'patient'
            session['phone number'] = '12345678'
        resp = c.post('/add/data', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)