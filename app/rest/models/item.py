from passlib.apps import custom_app_context as pwd_context
from . import db
import json

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", back_populates='items')

    def __repr__(self):
        return '<Item: %r, %r, %r>' %(self.id, self.name, self.quantity)

    def make_json(self):
        return json.dumps({
            "item_id": self.id,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "user_id": self.user_id
            })
