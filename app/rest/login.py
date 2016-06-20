from . import *

class LoginHandler(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('username', type = str, required = True, help = 'username is required', location = 'json')
        self.reqparser.add_argument('password', type = str, required = True, help = 'password is required', location = 'json')
        Resource.__init__(self)

    def get(self):
        args = self.reqparser.parse_args()
        print(args.get('username'), args.get('password'))
