# Toyolink

Toyolink offers a seamless solution for movie enthusiasts, alleviating the hassle of movie selection by consolidating your watched films and your corresponding ratings and reviews in one convenient hub. With Toyolink, users can effortlessly create an account, provide ratings and reviews for movies, explore films categorized by genres, and even discover movies tailored to the different genre preferences of two individuals.

## Quick Links

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup](#installation)
* [Future Goals](#future)

## <a name="tech-stack"></a>Tech Stack:

__Frontend:__ HTML, CSS, Javascript, jQuery <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>
__APIs:__ TMDb <br/>

## <a name="features"></a>Features:
  
Create an account or Login:
![Homepage](/static/img/homepage.jpg)
<br/><br/><br/>

Create a new account:
![Create An Account](/static/img/Registration.jpg)
<br/><br/><br/>

Login to your account:
![Login To Account](/static/img/Login.jpg)
<br/><br/><br/>
  
Browse through the entire movie selection:
![Browse All Movies](/static/img/AllMovies.jpg)
<br/><br/><br/>

Browse profile and ratings/reviews:
![Your Profile](/static/img/Profile.jpg)
<br/><br/><br/>

Browse the movies page and give a rating/review:
![Movie Pages](/static/img/MoviePage.jpg)
<br/><br/><br/>

Search the entire movie selection based on the chosen genre:
![Genre Search](/static/img/Genre.jpg)
<br/><br/><br/>

Search the entire movie selection based on two people's chosen genres:
![Movie Finder](/static/img/Finder.jpg)
<br/><br/><br/>

## <a name="installation"></a>Setup:

#### Requirements:

- PostgreSQL
- Python 3

To run this application do the following:

Clone repository:
```
$ git clone https://github.com/VeImore/Toyolink.git
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies🔗:
```
$ pip install -r requirements.txt
```