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
    return render_template('user_login.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account')

@app.route('/user_dash')
def user_dash():
    return render_template('user_dash')

@app.route('/user_list')
def user_list():
    return render_template('user_list')

@app.route('/movies_shows')
def movies_shows():
    return render_template('movies_shows')

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