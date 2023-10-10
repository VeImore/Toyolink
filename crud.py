from model import db, Users, User_List, Movies, Ratings_Reviews, Genres, Media_Genres, connect_to_db

def create_users(username, password):

    users = Users (username=username, password=password)

    return users

def create_user_list(users, movies):

    user_list = User_List (users=users, movies=movies)

    return user_list

def create_movies(content_id, 
                  title, 
                  tagline, 
                  director, 
                  genre, 
                  vote_average, 
                  year, 
                  media_type,
                  poster_path):

    movies = Movies(cotent_id=content_id, 
                    title=title, 
                    tagline=tagline, 
                    director=director, 
                    genre=genre, 
                    vote_average=vote_average, 
                    year=year, 
                    media_type=media_type,
                    poster_path=poster_path)
    return movies

def get_movies():

    return Movies.query.all()

def create_ratings(users, movies, rating):

    ratings_reviews = Ratings_Reviews (users=users, 
                                       movies=movies, 
                                       rating=rating)

    return ratings_reviews

def get_genres(genres, media_genres):

    genres = Genres (genres=genres, 
                     media_genres=media_genres)

    return genres.query.all()

def get_media_genres(movies, genres):

    media_genres = Media_Genres (movies=movies, 
                                 genres=genres)

    return media_genres.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)