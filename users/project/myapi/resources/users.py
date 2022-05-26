from flask_restful import Resource, reqparse
import requests
import psycopg2

import json

class Login(Resource):
    def get(self):
        """
        Get all users
        """
        one = False
        connection = psycopg2.connect("dbname= 'usersDB' user='admin' host='user-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchall()
        d:dict() = {}
        for item in row:
            d[item[0]] = item[1]
        return d

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="Invalid username")
        parser.add_argument('password', type=str, help="Invalid password")

        args = parser.parse_args()

        passedUserName = args['username']
        passedPassword = args['password']

        connection = psycopg2.connect("dbname= 'usersDB' user='admin' host='user-db' password='admin'")
        cursor = connection.cursor()
        #cursor.execute("SELECT * FROM users")
        cursor.execute("SELECT * FROM users WHERE user_name = %s AND user_password = %s", (passedUserName, passedPassword))

        row = cursor.fetchall()
        connection.close()

        if len(row) != 0:  # means there's a match
            return {"200 OK": "successful"}, 200
        else:
            return {"401 Unauthorized": "invalid credentials"}, 401  # unauthorized


class Register(Resource):
    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="Invalid username")
        parser.add_argument('password', type=str, help="Invalid password")

        args = parser.parse_args()

        passedUserName = args['username']
        passedPassword = args['password']

        connection = psycopg2.connect("dbname= 'usersDB' user='admin' host='user-db' password='admin'")
        cursor = connection.cursor()

        # Check first if user already exists
        cursor.execute("SELECT * FROM users WHERE user_name = %s", (passedUserName,))

        row = cursor.fetchall()
        if len(row) != 0:
            connection.close()
            return {"409 Conflict": "user already exists"}, 409
        else:
            cursor.execute("INSERT INTO users (user_name, user_password) VALUES (%s, %s)",
                           (passedUserName, passedPassword))
            connection.commit()
            connection.close()
            return {"200 OK": "Registered successfully"}, 200  # unauthorized


class AddFriend(Resource):
    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="Invalid username")
        parser.add_argument('friend_username', type=str, help="Invalid username")

        args = parser.parse_args()

        passedUserName = args['username']
        passedFriendUserName = args['friend_username']

        connection = psycopg2.connect("dbname= 'usersDB' user='admin' host='user-db' password='admin'")
        cursor = connection.cursor()

        # Check first if user already exists
        cursor.execute("SELECT * FROM users WHERE user_name = %s", (passedFriendUserName,))
        row = cursor.fetchall()
        if not row:
            connection.close()
            return {"404 Not Found": "user to be befriended does not exist"}, 404
        # Check if already friends
        cursor.execute("SELECT * FROM friends WHERE user_name = %s AND friend_name = %s",
                       (passedUserName, passedFriendUserName))
        row = cursor.fetchall()
        if len(row) != 0:
            connection.close()
            return {"409 Conflict": "user already befriended"}, 409
        else:
            cursor.execute("INSERT INTO friends (user_name, friend_name) VALUES (%s, %s)",
                           (passedUserName, passedFriendUserName))
            cursor.execute("INSERT INTO friends (friend_name, user_name) VALUES (%s, %s)",
                           (passedUserName, passedFriendUserName))
            connection.commit()
            connection.close()
            return {"200 OK": "Befriended succesfully"}, 200  # unauthorized

