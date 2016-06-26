from . import *
from .models.users import User
from .models import db
import os
import datetime

class LoginHandler(Resource):
    def __init__(self):
        super().__init__()
        self.reqparser = reqparse.RequestParser(bundle_errors=True)
        self.reqparser.add_argument('username', type = str, required = True, help = 'username is required', location = 'json')
        self.reqparser.add_argument('password', type = str, required = True, help = 'password is required', location = 'json')
        Resource.__init__(self)

    def get(self):
        args = self.reqparser.parse_args()

        user = db.session.query(User).filter_by(username=args.get('username')).first()

        if user:
            # user exists
            if user.check_passwd(args.get('password')):
                # correct password
                return jsonify({
                    "status": "login successful",
                    "api_token": user.generate_token()
                    })
            else:
                # wrong password
                return jsonify({
                    "status": "authentication error",
                    "error": "wrong password"
                    })
        else:
            # no such user
            return jsonify({
                'status': 'login unsuccessful',
                'error': 'no such user'
                })
        print(args.get('username'), args.get('password'))
