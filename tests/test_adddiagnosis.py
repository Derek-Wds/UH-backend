from tests.base import *

# Add personal detailed log
def test_add_diagnosis(data_regression):
    data = {
        'phone': '12345678',
        'title': 'Catch a cold',
        'content': 'I drink a lot of water today',
        'date': json.dumps(datetime(2020, 5, 17).__str__()),
        'diseases': {
            'cold': 'have a low fever for a week',
            'cough': 'have a sore throat for two days, and wants to drink water all the time'
        },
        't': 'detailed'}
    with app.test_client() as c:
        with c.session_transaction() as session:
            session['role'] = 'doctor'
            session['phone number'] = '11111111'
        resp = c.post('/add/diagnosis', data=json.dumps(data),
                       content_type='application/json')
        assert resp != None
        result = resp.get_json()
        DDID = result['diagnosis id']
        data_regression.check(result)