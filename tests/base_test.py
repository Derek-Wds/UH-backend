from tests.base import *

# Register doctor
def test_register_doctor(data_regression):
    data = {'username': 'Liu Cixin', 'phone': '11111111', 'password': 'test', 'role': 'doctor'}
    with app.test_client() as c:
        resp = c.post('/register', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)

# Register patient
def test_register_patient(data_regression):
    data = {'username': 'Han Han', 'phone': '12345678', 'password': 'test', 'role': 'patient'}
    with app.test_client() as c:
        resp = c.post('/register', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)

# Login doctor
def test_login_doctor(data_regression):
    data = {'phone': '11111111', 'password': 'test', 'role': 'doctor'}
    with app.test_client() as c:
        resp = c.post('/login', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)

# Login patient
def test_login_patient(data_regression):
    data = {'phone': '12345678', 'password': 'test', 'role': 'patient'}
    with app.test_client() as c:
        resp = c.post('/login', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)