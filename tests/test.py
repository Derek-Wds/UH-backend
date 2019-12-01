from tests.base import *
from database.database import db
from models import *

def test_delete():
    with app.app_context():
        Person.query.filter_by(phone='11111111').delete()
        Person.query.filter_by(phone='12345678').delete()
        Log.query.filter_by(id=ID).delete()
        Log.query.filter_by(id=DID).delete()
        Log.query.filter_by(id=DDID).delete()

        db.session.commit()