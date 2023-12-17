from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Toot(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    data = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False) # foreign key


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key
    username = db.Column(db.String(50), unique=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    birthday = db.Column(db.Integer)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))
    toot = db.relationship('Toot', backref='user', passive_deletes=True) # relate to Toot class
