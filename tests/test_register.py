from base import *

# Register doctor
def test_register_doctor():
    data = {'username': 'Liu Cixin', 'phone': '11111111', 'password': 'test', 'role': 'doctor'}
    resp = s.post(SERVER + '/register', data=data)
    assert resp != None
    result = json.loads(resp[0])
    assert result['status'] == 200 and result['msg'] == 'Success'

# Register patient
def test_register_patient():
    data = {'username': 'Han Han', 'phone': '12345678', 'password': 'test', 'role': 'patient'}
    resp = s.post(SERVER + '/register', data=data)
    assert resp != None
    result = json.loads(resp[0])
    assert result['status'] == 200 and result['msg'] == 'Success'