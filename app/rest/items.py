from . import *

class UserItems(Resource):
    def get(self, user_id):
        print(user_id)

class Items(Resource):
    def get(self, item_id):
        print(item_id)
