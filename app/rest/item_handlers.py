from . import *
from .auth import authorize, AuthHeaderParser
from .models.item import Item
from .models.users import User
from .models import db
from sqlalchemy import or_
import os

class UserItems(Resource, AuthHeaderParser):
    def __init__(self):
        super().__init__()
        # self.auth_parser.add_argument('username', type=int, required=True)

    @authorize
    def get(self, username):
        user = db.session.query(User.id).filter_by(username=username).first()

        if user:
            items = Item.query.filter_by(user_id=user.id).all()

            return jsonify({
                "status": "success",
                'data': [x.make_json() for x in items]
                })
        else:
            return jsonify({
                "status": "error",
                "message": "no such user"
                })

class ItemHandler(Resource, AuthHeaderParser):
    def __init__(self):
        super().__init__()

        self.update_parser = reqparse.RequestParser()
        self.update_parser.add_argument('name', type=str, location='json')
        self.update_parser.add_argument('description', type=str, location='json')
        self.update_parser.add_argument('quantity', type=int, location='json')

    @authorize
    def get(self, item_id):
        item = Item.query.filter_by(id=item_id).first()
        if item:
            # item exists
            return jsonify({
                "data": item.make_json()
                })
        else:
            # item does not exists
            return jsonify({
                "status": "error",
                "message": "item does not exists"
                })

    @authorize
    def put(self, item_id):
        item = Item.query.filter_by(id=item_id)

        if item[0]:
            # item exists
            # check if current user is provider of item
            if self.user_id == item[0].user_id:
                args = self.update_parser.parse_args()
                print(args)

                item.update({key:value for key, value in args.items() if value})

                db.session.commit()

                return jsonify({
                    "status": "success",
                    "update": item[0].make_json()
                    })

            else:
                # user is not owner of item
                return jsonify({
                    "status": "error",
                    "message": "operation not permitted"
                    })

        else:
            # item does not exists
            return jsonify({
                "status": "error",
                "message": "item does not exists"
                })
    @authorize
    def delete(self, item_id):
        item = Item.query.filter_by(id=item_id)

        if item[0]:
            # item exists
            # check owner
            if self.user_id == item[0].user_id:
                # user is owner, delete item
                db.session.delete(item[0])
                db.session.commit()
                return jsonify({
                    "status": "success",
                    "message": "successfully deleted item"
                    })
            else:
                # user is not owner
                return jsonify({
                    "ststus": "error",
                    "message": "opearation not permitted"
                    })

        else:
            # item does not exists
            return jsonify({
                "status": "error",
                "message": "item does not exists"
                })

class CreateItem(Resource, AuthHeaderParser):
    def __init__(self):
        super().__init__()

        self.auth_parser.add_argument('item_name', type=str, required=True, location='json')
        self.auth_parser.add_argument('description', type=str, location='json')
        self.auth_parser.add_argument('quantity', type=int, required=True, location='json')

    @authorize
    def post(self):
        args = self.auth_parser.parse_args()

        item = Item(name=args.get('item_name'),
                description=args.get('description', ''),
                quantity=args.get('quantity'),
                user_id=self.user_id)

        db.session.add(item)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "successfully added item",
            "item_id": item.id
            })

class Search(Resource, AuthHeaderParser):
    @authorize
    def get(self, search_query):
        print(search_query)

        results = db.session.query(Item).filter(or_(Item.name.contains(search_query),
            Item.description.contains(search_query))).all()

        return jsonify({
            "data": [result.make_json() for result in results]
            })
