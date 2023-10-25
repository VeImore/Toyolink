from model import db, User, Movie, Rating, connect_to_db

def create_users(username, password):

    user = User (username=username, password=password)

    return user

def create_movie(content_id, 
                  title, 
                  tagline, 
                  vote_average, 
                  year, 
                  media_type,
                  poster_path):
    
    movie = Movie(content_id=content_id, 
                    title=title, 
                    tagline=tagline, 
                    vote_average=vote_average, 
                    year=year, 
                    media_type=media_type,
                    poster_path=poster_path)
    return movie

def create_rating(users, movie, score):

    rating = Rating(users=users, 
                    movie=movie, 
                    score=score)

    return rating

def get_movies():

    return Movie.query.all()

def get_movie_by_id(content_id):

    return Movie.query.get(content_id)

def get_users():

    return User.query.all()

def get_users_profile(user_id):

    return User.query.get(user_id)

def get_user_by_username(username):

    return User.query.filter(User.username == username).first()

def get_user_ratings(user_id):
    
    user = User.query.get(user_id)

    if user is None:
        return []
    
    user_ratings_records = Rating.query.filter_by(user_id=user_id).all()
    user_ratings = [(record.movie, record.score) for record in user_ratings_records]
    
    return user_ratings


# def get_genres(genres, media_genres):

#     genres = Genres (genres=genres, 
#                      media_genres=media_genres)

#     return genres.query.all()

# def get_media_genres(movie, genres):

#     media_genres = Media_Genres (movie=movie, 
#                                  genres=genres)

#     return media_genres.query.all()

# def get_genre_by_name(name):

#     return  Genres.query.filter_by(genre=name).first()

# def create_genre(genre_by_name):

#     new_genre = Genres(genre=genre_by_name)

#     return new_genre

# def create_media_genre(movie, genres):
    
#     new_media_genre = Media_Genres(movie=movie, genres=genres)

#     return new_media_genre

# def get_user_by_username(username):
    
#     return User.query.filter(User.username == username).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)