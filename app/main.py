import os
from rest.models import db
from itsdangerous import JSONWebSignatureSerializer as JWS

from rest import api, app
from rest.login import LoginHandler
from rest.signup import SignupHandler, CheckExistingUser
from rest.items import UserItems, ItemHandler, CreateItem

api.add_resource(LoginHandler, '/login')
api.add_resource(SignupHandler, '/signup')
api.add_resource(UserItems, '/<string:username>')
api.add_resource(ItemHandler, '/item/<int:item_id>')
api.add_resource(CreateItem, '/item/create')
api.add_resource(CheckExistingUser, '/check_existing/<string:username>')

# setting up token mechanism
try:
    app.secret_key = os.environ['SECRET_KEY']
    JWT = JWS(app.secret_key)
except KeyError:
    print('Please set the secret_key')
    exit()

#initialize orm
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# for debugging
def create_app():
    with app.app_context():
        db.create_all()
    return app

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
