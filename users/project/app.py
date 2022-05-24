# this file is purely for development
from flask import Flask
from project.myapi.resources.users import Login
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(Login, '/api/login')

@app.route("/")
def hello():
    return "Hi there!"
