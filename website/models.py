from . import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Date

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    fname = db.Column(db.String(150))
    mname = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    age = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date = db.Column(Date, default=datetime.utcnow)
    bday = db.Column(db.DateTime(timezone=True))
    mstatus = db.Column(db.String(150)) 
    address = db.Column(db.String(150))
    phid = db.Column(db.String(150))
    records = db.relationship('Records', backref='users')
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    note = db.Column(db.String(150))
    doctor = db.Column(db.String(150))
    validated = db.Column(db.String(150))
    date = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    filename = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

