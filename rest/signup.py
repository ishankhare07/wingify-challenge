from . import *
from .models import db
from .models.users import User

class SignupHandler(Resource):
    def __init__(self):
        super().__init__()
        self.reqparser = reqparse.RequestParser(bundle_errors=True)

        self.reqparser.add_argument('firstname', type = str, required = True, help = 'User must have a firstname', location = 'json')
        self.reqparser.add_argument('lastname', type = str, required = True, help = 'Lastname is required', location = 'json')
        self.reqparser.add_argument('username', type = str, required = True, help = 'username is required', location = 'json')
        self.reqparser.add_argument('password', type = str, required = True, help = 'password is required', location = 'json')

    def post(self):
        data = self.reqparser.parse_args()

        user = User(data['firstname'],
                data['lastname'],
                data['username'],
                data['password'])

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "status": "signup succesful",
            "api_token": user.generate_token()
            })

class CheckExistingUser(Resource):
    def get(self, username):
        data = db.session.query(User.username).filter_by(username=username).all()
        print(data)
        if data:
           # username exists
           return jsonify({
               "status": "error",
               "message": "username already exists"
               })
        else:
            return jsonify({
                "status": "success",
                "message": "{0} unique".format(username)
                })
