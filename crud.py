from model import db, Users, User_List, Movies_Shows, Ratings_Reviews, Genres, Media_Genres, connect_to_db

def create_users(username, email, password):

    users = Users (username=username, email=email, password=password)

    return users

def create_user_list(users, movies_shows):

    user_list = User_List (users=users, movies_shows=movies_shows)

    return user_list

def create_movies_shows(title, director, genre, rating, year, media_type):

    movies_shows = Movies_Shows (title=title, director=director, genre=genre, rating=rating, year=year, media_type=media_type)

    return movies_shows

def create_ratings_reviews(users, movies_shows, rating, review):

    ratings_reviews = Ratings_Reviews (users=users, movies_shows=movies_shows, rating=rating, review=review)

    return ratings_reviews

def create_genres(genres, media_genres):

    genres = Genres (genres=genres, media_genres=media_genres)

    return genres

def create_media_genres(movies_shows, genres):

    media_genres = Media_Genres (movies_shows=movies_shows, genres=genres)

    return media_genres

if __name__ == '__main__':
    from server import app
    connect_to_db(app)