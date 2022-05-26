# this file is purely for development
from flask import Flask
from project.myapi.resources.users import Login
from project.myapi.resources.users import Register
from project.myapi.resources.users import AddFriend
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(AddFriend, '/api/addFriend')

@app.route("/")
def hello():
    return "Hi there!"
