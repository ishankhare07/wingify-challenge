from passlib.apps import custom_app_context as pwd_context
from . import db
from itsdangerous import JSONWebSignatureSerializer as JWS
import os
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True)

    items = db.relationship("Item", back_populates='user')

    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password_hash = pwd_context.encrypt(password)

    def __repr__(self):
        return '<User: %r>' % self.username

    def check_passwd(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_token(self):
        JWT = JWS(os.environ.get('SECRET_KEY'))
        return JWT.dumps({
            "id": self.id,
            "username": self.username,
            # 2 hrs expiration
            "expires": (datetime.datetime.now() +
                        datetime.timedelta(seconds=2*60*60)).timestamp()
            }).decode('utf-8')
