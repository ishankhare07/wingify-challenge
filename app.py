import os
from rest.models import db
from itsdangerous import JSONWebSignatureSerializer as JWS

from rest import api, app
from rest.login import LoginHandler
from rest.signup import SignupHandler, CheckExistingUser
from rest.item_handlers import UserItems, ItemHandler, CreateItem, Search

api.add_resource(LoginHandler, '/login')
api.add_resource(SignupHandler, '/signup')
api.add_resource(UserItems, '/<string:username>')
api.add_resource(ItemHandler, '/item/<int:item_id>')
api.add_resource(CreateItem, '/item/create')
api.add_resource(CheckExistingUser, '/check_existing/<string:username>')
api.add_resource(Search, '/search/<string:search_query>')

# check secret key for JSON web tokens
try:
    os.environ['SECRET_KEY']
except KeyError:
    print('Please set the secret_key')
    exit()

#initialize orm
db.init_app(app)

try:
    # for deploying on heroku
    database_url = os.environ['DATABASE_URL']
except KeyError:
    # running locally
    database_url = 'sqlite:///test.db'

app.config['SQLALCHEMY_DATABASE_URI'] = database_url

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
