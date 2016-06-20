from . import *

class SignupHandler(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()

        self.reqparser.add_argument('firstname', type = str, required = True, help = 'User must have a firstname', location = 'json')
        self.reqparser.add_argument('lastname', type = str, required = True, help = 'Lastname is required', location = 'json')
        self.reqparser.add_argument('username', type = str, required = True, help = 'username is required', location = 'json')
        self.reqparser.add_argument('password', type = str, required = True, help = 'password is required', location = 'json')

    def post(self):
        data = self.reqparser.parse_args()
        print(data)
