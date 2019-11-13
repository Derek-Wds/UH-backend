from base import *

# Register staff
def test_register_staff():
    data = {'name': 'Liu Cixin', 'public_key': 'notadoctor', 'device_id': 1}
    resp = s.post(SERVER + 'register/staff', data=data)
    assert resp != None
    result = json.loads(resp.text)
    assert result['status'] == 1 and result['message'] == 'Success.'