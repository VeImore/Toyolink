from flask import (Flask, render_template, request, flash, session, redirect, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

from model import connect_to_db, db, Movie, Genre, User, Rating, Media_Genres
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

users = {}

@app.route('/')
def homepage():

    return render_template('homepage.html')

@app.route('/movies_by_genre', methods=['GET', 'POST'])
def show_movies_by_genre():
    selected_genre = request.args.get('genre')
    if request.method == 'POST':
        selected_genre = request.form['genre']
        return redirect(url_for('show_movies_by_genre', genre=selected_genre))

    if selected_genre:
        genre_obj = Genre.query.filter_by(genre=selected_genre).first()
        if genre_obj:
            movies = [mg.movie for mg in genre_obj.media_genres]
        else:
            flash('Genre not found!')
            return redirect(url_for('show_movies_by_genre'))
    else:
        movies = Movie.query.all()

    genres = [genre_obj.genre for genre_obj in Genre.query.all()]

    return render_template('movies_by_genre.html', movies=movies, genres=genres, selected_genre=selected_genre)

@app.route("/movies/<content_id>")
def show_movie(content_id):
    """Show details on a particular movie."""

    movie= crud.get_movie_by_id(content_id)

    return render_template("movie_page.html", movie=movie)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!')
            return redirect(url_for('register'))
 
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.user_id 
            return redirect(url_for('show_movies'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    
    return render_template('user_login.html')

@app.route('/user/<user_id>')
def user_profile(user_id):

    user_ratings = crud.get_user_ratings(user_id)
    return render_template('user_profile.html', user_ratings=user_ratings)

@app.route('/user_login')
def user_login():

    return render_template('user_login.html')

@app.route('/create_account')
def create_account():

    return render_template('create_account.html')

@app.route('/all_movies', methods=['GET', 'POST'])
def show_movies():
    selected_genre = None
    user_id = session['user_id']
    if request.method == 'POST':
        selected_genre = request.form['genre']
    if selected_genre:
        movies = Movie.query.filter_by(genre=selected_genre).all()
    else:
        movies = Movie.query.all()
    genres = Genre.query.all()
    return render_template('all_movies.html', user_id=user_id, movies=movies, genres=genres)

@app.route("/movies/<content_id>/rate", methods=['POST'])
def rate_movie(content_id):
    """Handle rating submission for a movie."""
    
    user_id = session.get('user_id')
    if not user_id:
        flash("Please login first!")
        return redirect(url_for('login'))
    
    rating = request.form['rating']
    review = request.form['review']
    
    movie_rating = Rating(rating=rating, review=review, user_id=user_id, content_id=content_id)
    db.session.add(movie_rating)
    db.session.commit()
    
    flash('Rating and Review submitted successfully!')
    return redirect(url_for('show_movie', content_id=content_id))

from random import choice

@app.route('/movie_finder', methods=['GET', 'POST'])
def movie_finder():
    movies = []
    
    if request.method == 'POST':

        first_half = [
            request.form['genre1'],
            request.form['genre2'],
            request.form['genre3']
        ]
        second_half = [
            request.form['genre4'],
            request.form['genre5'],
            request.form['genre6']
        ]
        
        selected_genre1 = choice([g for g in first_half if g])
        selected_genre2 = choice([g for g in second_half if g])

        movies1 = set([mg.movie for mg in Media_Genres.query.filter_by(genre_id=selected_genre1).all()])
        movies2 = set([mg.movie for mg in Media_Genres.query.filter_by(genre_id=selected_genre2).all()])

        movies = list(movies1.intersection(movies2))

        genres = Genre.query.all()
        return render_template('movie_finder.html', movies=movies, genres=genres)

    genres = Genre.query.all()
    return render_template('movie_finder.html', movies=movies, genres=genres)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", port=5555, debug=True)