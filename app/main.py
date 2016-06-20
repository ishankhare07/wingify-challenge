from rest import api, app
from rest.login import LoginHandler
from rest.signup import SignupHandler
from rest.items import UserItems, Items

api.add_resource(LoginHandler, '/login')
api.add_resource(SignupHandler, '/signup')
api.add_resource(UserItems, '/<int:user_id>')
api.add_resource(Items, '/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
