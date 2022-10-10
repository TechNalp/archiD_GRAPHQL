import json

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."),"r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open("{}/data/movies.json".format("."),"r") as rfile:
        movies = json.load(rfile)
        for movie in movies["movies"]:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open("{}/data/movies.json".format("."),"w") as wfile:
        json.dump(newmovies,wfile)
    return newmovie


def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format('.'),"r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def all_movies(_,info):
    with open('{}/data/movies.json'.format("."),"r") as file:
        data = json.load(file)
        print(data["movies"])
        return data["movies"]


def create_movie(_,info,input):
    if not input["id"] or not input["title"] or not input["director"] or not (input["rating"] >=0.0 and input["rating"] <=10.0):
        return {"id":"","title":"","director":"","rating":-1}
    with open('{}/data/movies.json'.format("."),"r") as file:
        data = json.load(file)
    for movie in data["movies"]: # On vérifie que l'id est disponible
        if movie["id"] == input["id"]:
            return {"id": "", "title": "", "director": "", "rating": -1} # Si l'id est déjà pris
    newMovie = {"id": input["id"], "title": input["title"], "director": input["director"], "rating": float(input["rating"])}
    data["movies"].append(newMovie)
    with open('{}/data/movies.json'.format("."),"w") as file:
        json.dump(data,file)
    return newMovie


def delete_movie(_,info,_id):
    if not _id:
        return ""
    with open('{}/data/movies.json'.format("."), "r") as file:
        data = json.load(file)
    for movie in data["movies"]:
        if movie["id"] == _id:
            data["movies"].remove(movie)
            with open("{}/data/movies.json".format("."),"w") as file:
                json.dump(data,file)
            return movie["id"]
    return ""


def movie_with_title(_,info,_title):
    if not _title:
        return {"id": "", "title": "", "director": "", "rating": -1}
    with open('{}/data/movies.json'.format("."), "r") as file:
        data = json.load(file)
    for movie in data["movies"]:
        if movie["title"].lower() == _title.lower():
            return movie
    return {"id": "", "title": "", "director": "", "rating": -1}