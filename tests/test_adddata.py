from base import *

# Add personal data
def test_add_data():
    data = {}
    resp = s.post(SERVER + '/add/data', data=data)
    assert resp != None
    result = json.loads(resp[0])
    assert result['status'] == 200 and result['msg'] == 'Success'