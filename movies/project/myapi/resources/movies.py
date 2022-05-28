from flask_restful import Resource, reqparse
import requests
import psycopg2

import json


class GetMovies(Resource):
    def get(self):
        """
                Get all movies
        """
        connection = psycopg2.connect("dbname= 'moviesDB' user='admin' host='movie-db' password='admin'")
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM movies")
        row = cursor.fetchall()
        movieList = []
        for movie in row:
            movieList.append(movie[0])
        return {"movies": movieList}, 200