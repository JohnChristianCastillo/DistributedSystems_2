from flask_restful import Resource, reqparse
import requests
import psycopg2

import json


class CreateGroup(Resource):
    def get(self):
        # todo: delete this
        """
        Get all groups
        """
        connection = psycopg2.connect("dbname= 'groupsDB' user='admin' host='group-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM groups")
        row = cursor.fetchall()
        d:dict() = {}
        for item in row:
            d[item[0]] = item[1]
        connection.close()
        return d

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('group_name', type=str, help="Invalid group_name")
        parser.add_argument('owner_username', type=str, help="Invalid owner_username")

        args = parser.parse_args()

        passedUserName = args['owner_username']
        passedGroupName = args['group_name']

        connection = psycopg2.connect("dbname= 'groupsDB' user='admin' host='group-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM groups WHERE owner_username = %s AND group_name = %s", (passedUserName, passedGroupName))
        row = cursor.fetchall()

        if len(row) != 0:  # means there's a match
            connection.close()
            return {"409 Conflict": "You already made a group with the same name"}, 409
        else:
            cursor.execute("INSERT INTO groups (group_name, owner_username) VALUES (%s, %s)",
                           (passedGroupName, passedUserName))
            connection.commit()
            connection.close()
            return {"200 OK": "Group registered successfully"}, 200


class AddFriendToGroup(Resource):
    """
    The first thing to consider for this API is: Whose task is it to verify if the user being added
    is indeed a friend of the group owner. Do we verify it here by sending a request to the users microservice
    or do we just assume it is already verified
    """
    def get(self):
        """
        Get all groups
        """
        connection = psycopg2.connect("dbname= 'groupsDB' user='admin' host='group-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members")
        row = cursor.fetchall()
        d: dict() = {}
        for item in row:
            d[item[0]] = item[1]
        connection.close()
        return d

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('group_name', type=str, help="Invalid group_name")
        parser.add_argument('owner_username', type=str, help="Invalid owner_username")
        parser.add_argument('friend_username', type=str, help="Invalid friend_username")

        args = parser.parse_args()

        passedUserName = args['owner_username']
        passedGroupName = args['group_name']
        passedFriendUserName = args['friend_username']

        connection = psycopg2.connect("dbname= 'groupsDB' user='admin' host='group-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM groups WHERE group_name = %s ",
                       (passedGroupName, ))
        row = cursor.fetchall()

        if len(row) == 0:  # means there's no such group
            return {"404 Not Found": f"Group with group_name:{passedGroupName} does not exist"}, 404

        # check if friend is already a member
        cursor.execute("SELECT * FROM members WHERE group_name = %s AND member_name = %s",
                       (passedGroupName, passedFriendUserName))
        row = cursor.fetchall()
        if len(row) != 0:
            connection.close()
            return {"409 Conflict": f"Friend with user_name:{passedFriendUserName} is already a member of the group"}, 409

        else:
            cursor.execute("INSERT INTO members (group_name, member_name) VALUES (%s, %s)",
                           (passedGroupName, passedFriendUserName))
            connection.commit()
            connection.close()
            return {"200 OK": "Friend invited successfully"}, 200
