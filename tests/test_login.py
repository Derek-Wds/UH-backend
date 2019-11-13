from base import *

# Login doctor
def test_login_doctor():
    data = {'phone': '11111111', 'password': 'test'}
    resp = s.post(SERVER + '/login', data=data)
    assert resp != None
    result = json.loads(resp[0])
    assert result['status'] == 200 and result['msg'] == 'Success'

# Login patient
def test_login_patient():
    data = {'phone': '12345678', 'password': 'test'}
    resp = s.post(SERVER + '/login', data=data)
    assert resp != None
    result = json.loads(resp[0])
    assert result['status'] == 200 and result['msg'] == 'Success'
