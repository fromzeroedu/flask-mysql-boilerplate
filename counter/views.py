from flask import Blueprint

from application import db
from counter.models import Counter

counter_app = Blueprint('counter_app', __name__)

@counter_app.route('/')
def init():
    counter = Counter.query.first()
    if not counter:
        counter = Counter(1)
        db.session.add(counter)
        db.session.commit()
    else:
        counter.count += 1
        db.session.commit()
    return "<h1>Counter: " + str(counter.count) + "</h1>"
