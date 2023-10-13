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

@app.route('/movies')
def all_movies():

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route("/movies/<content_id>")
def show_movie(content_id):
    """Show details on a particular movie."""

    movie= crud.get_movie_by_id(content_id)

    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def display_users():
    """Show all users"""
    users = crud.get_users()

    return render_template(".html", users=users)

@app.route('/users', methods=["POST"])
def register_user():

    username = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route('/login', methods=["POST"])
def login_user():
    """Log user in"""
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if not user or user.password != password:
        flash("This username or password you entered is incorrect.")
    else:
        session["user_username"] = user.username
        flash(f"Welcome back {user.username}!")
    
    return redirect('/movies')

@app.route('/user_login')
def user_login():

    return render_template('user_login.html')

@app.route('/create_account')
def create_account():

    return render_template('create_account.html')

@app.route('/user_dash')
def user_dash():

    return render_template('user_dash.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)