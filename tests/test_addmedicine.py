from tests.base import *

# Add medicine
def test_add_medicine(data_regression):
    data = {
        'patient_phone': '12345678',
        'name': 'aspirin',
        'description': 'test',
        'times': {
            '1': '9:00 A.M.',
            '2': '12:00 P.M.',
            '3': '6:00 P.M.'
            }
        }
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'doctor'
            session['phone number'] = '11111111'
        resp = c.post('/add/medicine', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        data_regression.check(result)