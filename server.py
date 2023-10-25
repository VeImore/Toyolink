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
        movies = [mg.movie for mg in genre_obj.media_genres]
        #movies = genre_obj.get_movies() if genre_obj else []
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

@app.route('/rate_movie/<content_id>', methods=['POST'])
def rate_movie(content_id):
    user_id = session['user_id']
    user = User.query.get(user_id)
    movie = Movie.query.get(content_id)

    if not user or not movie:
        flash('Error Rating Movie.')
        return redirect(url_for('hoempage'))
    
    rating_value = request.form['rating']
    review_text = request.form['review']

    rating = Rating(user=user, movie=movie, rating=rating, review=review_text)

    db.session.add(rating)
    db.session.commit()

    flash('Rating Submitted.')
    return redirect(url_for('user_profile', user_id=user_id))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)