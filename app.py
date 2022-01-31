import os


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://pvoximlfppsbaa:618f39d0ed0f264d42120007be1c884c658b82ade223310d3b153547dbfd1746@ec2-54-157-15-228.compute-1.amazonaws.com:5432/d83f1r1i8se68d','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vareesh'
api = Api(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

jwt = JWT(app, authenticate, identity) #/auth created


api.add_resource(Item, '/item/<string:name>')  #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')  #http://127.0.0.1:5000/items
api.add_resource(UserRegister,'/register') 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':

    app.run(port=5000, debug=True)

