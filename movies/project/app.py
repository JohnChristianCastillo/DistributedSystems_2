# this file is purely for development
from flask import Flask
from project.myapi.resources.movies import GetMovies
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(GetMovies, '/api/getMovies')

@app.route("/")
def hello():
    return "This is the 'movies' microservice"
