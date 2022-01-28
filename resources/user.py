from dataclasses import dataclass
import sqlite3
import string
from flask_restful import Resource,reqparse
from flask import request
from models.user_models import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('password', type=str, required=True, help = "This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message' : "Username already exists"}, 400
        # else:
        #     connection = sqlite3.connect('data.db')
        #     cursor = connection.cursor()
        #     query = "INSERT INTO users VALUES (null,?,?)"
        #     cursor.execute(query,(data['username'],data['password']))

        #     connection.commit()
        #     connection.close()
        user = UserModel(**data)
        user.save_to_db()

        return {'message': "User Registered Successfully."}, 201

