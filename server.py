from flask import (Flask, render_template, request, flash, session, redirect, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

from model import connect_to_db, db, Movie, Genre, Media_Genres
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
    selected_genre = request.args.get('genre')  # Use URL parameter to get the genre
    if request.method == 'POST':
        selected_genre = request.form['genre']
        # Redirect to the same route with the genre as a URL parameter
        return redirect(url_for('show_movies_by_genre', genre=selected_genre))

    if selected_genre:
        movies = Movie.query.filter_by(genre=selected_genre).all()
    else:
        movies = Movie.query.all()
    
    genres = Genre.query.all()  # Fetch genres outside the else block

    return render_template('movies_by_genre.html', movies=movies, genres=genres, selected_genre=selected_genre)

@app.route("/movies/<content_id>")
def show_movie(content_id):
    """Show details on a particular movie."""

    movie= crud.get_movie_by_id(content_id)

    return render_template("movie_page.html", movie=movie)

@app.route('/users')
def display_users():
    """Show all users"""
    users = crud.get_users()

    return render_template(".html", users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']

        if username in users:
            flash('Username already exists!')
            return redirect(url_for('register'))
 
        hashed_password = generate_password_hash(password, method='sha256')
        users[username] = hashed_password

        flash('Registration successful!')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            return redirect(url_for('show_movies'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    
    return render_template('user_login.html')

@app.route('/users/<user_id>')
def show_user(user_id):

    users = crud.get_users_profile(user_id)

    return render_template("user_profile.html", user=users)

@app.route('/user_login')
def user_login():

    return render_template('user_login.html')

@app.route('/create_account')
def create_account():

    return render_template('create_account.html')

@app.route('/all_movies', methods=['GET', 'POST'])
def show_movies():
    selected_genre = None
    if request.method == 'POST':
        selected_genre = request.form['genre']
    if selected_genre:
        movies = Movie.query.filter_by(genre=selected_genre).all()
    else:
        movies = Movie.query.all()
    genres = Genre.query.all()
    return render_template('all_movies.html', movies=movies, genres=genres)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)