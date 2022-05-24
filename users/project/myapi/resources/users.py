from flask_restful import Resource, reqparse
import requests


class Login(Resource):
    def get(self):
        return {"Hello there": "h"}, 200


class Register(Resource):
    def get(self):
        pass

    def post(self):
        pass