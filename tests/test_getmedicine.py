from tests.base import *

# Get medicine
def test_get_medicine(data_regression):
    data = {
        'patient_phone': '12345678'
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'doctor'
            session['phone number'] = '11111111'
        resp = c.post('/get/medicine', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)