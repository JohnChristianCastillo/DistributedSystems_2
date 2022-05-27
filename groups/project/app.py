# this file is purely for development
from flask import Flask
from project.myapi.resources.groups import CreateGroup
from project.myapi.resources.groups import AddFriendToGroup
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(CreateGroup, '/api/createGroup')
api.add_resource(AddFriendToGroup, '/api/addFriendToGroup')

@app.route("/")
def hello():
    return "This is the 'groups' microservice"
