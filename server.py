from flask import (Flask, render_template, request, flash, session, redirect)
app = Flask(__name__)

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/user_login')
def user_login():

    username = request.form.get("username")
    password = request.form.get("password")

    return render_template('user_login.html')

@app.route('/create_account')
def create_account():

    return render_template('create_account.html')

@app.route('/user_dash')
def user_dash():

    return render_template('user_dash.html')

@app.route('/user_list')
def user_list():

    return render_template('user_list')

@app.route('/movies')
def all_movies():

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/shows')
def shows():

    return render_template('shows')

@app.route('/ratings_reviews')
def ratings_reviews():

    return render_template('ratings_reviews')

@app.route('/genres')
def genres():

    return render_template('genres')

@app.route('/couple_movies')
def couple_movies():

    return render_template('couple_movies')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)