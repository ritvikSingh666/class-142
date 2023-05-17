from flask import Flask, jsonify, request
import csv 

all_movies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    
    data = list(reader)

    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []


app = Flask(__name__)

@app.route("/get-movie")

def getmovie():
    return jsonify({
        "data": all_movies[0],
        "status": "success",
        
        
    })

@app.route("/liked-movies", methods = ["POST"])
def likedmovies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201


@app.route("/unliked_movies", methods = ["POST"])
def unlikedmovies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }),201


@app.route("/not-watched-movies", methods = ["POST"])
def notwatchedmovies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }),201

if __name__ == "__main__":
    app.run()



