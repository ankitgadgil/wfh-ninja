from main import app, db
from flask import *

import simplejson as json
import uuid

# class Paste(db.Model):
#     id = db.Column(db.String(36), unique=True, primary_key=True)
#     poster = db.Column(db.String(51))
#     paste = db.Column(db.Text())

#     def __init__(self, text, poster="Anonymous"):
#         self.paste = text
#         self.id = str(uuid.uuid4())

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(500))
    conditions = db.Column(db.Text)
    date_created = db.Column(db.DateTime)
    view_count = db.Column(db.Integer)

    def __init__(self, text, conditions, date_created, view_count):
        self.text = text
        self.conditions = conditions
        self.date_created = date_created
        self.view_count = view_count

    def __repr__(self):
        return json.dumps({"id": self.id, "text": self.text, "conditions": self.conditions, "date_created": self.date_created, "view_count": self.view_count})

    @property
    def serialize(self):
        return {"id": self.id, "text": self.text, "conditions": self.conditions, "date_created": self.date_created.isoformat(), "view_count": self.view_count}
    


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.String(15))
    value = db.Column(db.Integer)
    quote_id = db.Column(db.Integer, db.ForeignKey('quote.id'))

    def __init__(self, id, ip, value, quote_id):
        self.id = id
        self.ip = ip
        self.value = value
        self.quote_id = quote_id

    def __repr__(self):
        return json.dumps({"id": self.id, "ip": self.ip, "value": self.value, "quote_id": self.quote_id})