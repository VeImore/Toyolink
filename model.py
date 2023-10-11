from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///Toyolink", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

class Users(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    user_list = db.relationship("User_List", back_populates="users")
    ratings_reviews = db.relationship("Ratings_Reviews", back_populates="users")

    def __repr__(self):
        return f'<Users user_id={self.user_id} username={self.username} email={self.email}>'   

class User_List(db.Model):

    __tablename__ = "user_list"

    list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    content_id = db.Column(db.String, db.ForeignKey("movies.content_id"))

    users = db.relationship("Users", back_populates="user_list")
    movies = db.relationship("Movies", back_populates="user_list")

    def __repr__(self):
        return f'<User_List list_id={self.list_id} user_id={self.user_id} content_id={self.content_id}>'
    
class Movies(db.Model):

    __tablename__ = "movies"

    content_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    tagline = db.Column(db.String)
    director = db.Column(db.String, nullable=True)
    genre = db.Column(db.String, nullable=True)
    vote_average = db.Column(db.Integer)
    year = db.Column(db.String)
    media_type = db.Column(db.String)
    poster_path = db.Column(db.String)

    user_list = db.relationship("User_List", back_populates="movies")
    ratings_reviews = db.relationship("Ratings_Reviews", back_populates="movies")
    media_genres = db.relationship("Media_Genres", back_populates="movies")

    def __repr__(self):
        return f'<Movies content_id={self.content_id} title={self.title} director={self.director} genre={self.genre} rating={self.rating} media_type={self.media_type} api_id={self.api_id}>'

class Ratings_Reviews(db.Model):

    __tablename__ = "ratings_reviews"

    ratings_reviews_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    content_id = db.Column(db.String, db.ForeignKey("movies.content_id"))

    users = db.relationship("Users", back_populates="ratings_reviews")
    movies = db.relationship("Movies", back_populates="ratings_reviews")

    def __repr__(self):
        return f'<Ratings_Reviews ratings_reviews_id={self.ratings_reviews_id} rating={self.rating} review={self.review} user_id={self.user_id} content_id={self.content_id}>'

class Genres(db.Model):

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String)

    media_genres = db.relationship("Media_Genres", back_populates="genres")

class Media_Genres(db.Model):

    __tablename__ = "media_genres"

    media_genres_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.String, db.ForeignKey("movies.content_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))
    
    movies = db.relationship("Movies", back_populates="media_genres")
    genres = db.relationship("Genres", back_populates="media_genres")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)