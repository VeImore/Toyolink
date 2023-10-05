from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

class Users(db.Model):

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<Users user_id={self.user_id} username={self.username} email={self.email}>'   

class List(db.Model):

    list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key=True)
    content_id = db.Column(db.String, foreign_key=True)

    def __repr__(self):
        return f'<List list_id={self.list_id} user_id={self.user_id} content_id={self.content_id}>'
    
class Movies_Shows(db.Model):

    content_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, unique=True)
    director = db.Column(db.String, unique=True)
    genre = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    type = db.Column(db.String)
    API_id = db.Column(db.String)

    def __repr__(self):
        return f'<Movies_Shows content_id={self.content_id} title={self.title} director={self.director} genre={self.genre} rating={self.rating} type={self.type} API_id={self.API_id}>'

class Ratings_Reviews(db.Model):

    ratings_reviews_id = db.Column(db.Integer)
    rating = db.Column(db.Integer, unique=True)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, foreign_key=True)
    content_id = db.Column(db.Integer, foreign_key=True)

    def __repr__(self):
        return f'<Ratings_Reviews ratings_reviews_id={self.ratings_reviews_id} rating={self.rating} review={self.review} user_id={self.user_id} content_id={self.content_id}>'

if __name__ == "__main__":
    from server import app

    connect_to_db(app)