from flask_restful import Resource, reqparse
import requests
import psycopg2

import json

class Login(Resource):
    def get(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\nHello")

    def post(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\nHello")
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="Invalid username")
        parser.add_argument('password', type=str, help="Invalid password")

        args = parser.parse_args()

        passedUserName = args['username']
        passedPassword = args['password']

        connection = psycopg2.connect("dbname= 'usersDB' user='admin' host='user-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")

        row = cursor.fetchall()
        for user in row:
            if user[0] == passedUserName and user[1] == passedPassword:
                return {"valid": "successful"}, 200

        return {"invalid": "invalid credentials"}, 401  # unauthorized


class Register(Resource):
    def get(self):
        pass

    def post(self):
        pass