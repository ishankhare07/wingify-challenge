from functools import wraps
from . import jsonify, reqparse
from itsdangerous import (
        JSONWebSignatureSerializer as JWS,
        BadSignature)
import os
import datetime

class AuthHeaderParser:
    def __init__(self):
        self.auth_parser = reqparse.RequestParser(bundle_errors=True)
        self.auth_parser.add_argument('Authorization', type=str, required=True,
                help='Authorization header needs to be set with api token',
                location='headers', dest='api_token')

def authorize(f, *args, **kwargs):
    @wraps(f)
    def check_authorization(*args, **kwargs):
        instance = args[0]          # self argument
        request_args = instance.auth_parser.parse_args()

        token = request_args.get('api_token')

        # parse token
        JWT = JWS(os.environ.get('SECRET_KEY'))
        try:
            token_data = JWT.loads(token)
        except BadSignature:
            return jsonify({
                'status': 'auth error',
                'message': 'invalid token'
                })

        # check validation
        if datetime.datetime.now().timestamp() < token_data.get('expires'):
            # token valid and not expired
            # add current user id to instance as an attribute
            # this allows linking items to users with re-parsing the tokens
            instance.user_id = token_data.get('id')
            return f(*args, **kwargs)
        else:
            # token expired
            return jsonify({
                'status': 'auth error',
                'message': 'token expired',
                'help': 'get a new token generated from login endpoint'
                })
    return check_authorization
