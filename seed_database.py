import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server



os.system('dropdb Toyolink')
os.system('createdb Toyolink')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
# Loop through each movie in the JSON file
for movie in movie_data:
    #-----------------
    # GOAL: Create a list of Genre objects to correspond with this movie

    genre_lst = [] # Make an empty list to hold all the genres for this movie
    for genre in movie["genres"]: # For each genre listed in the JSON file                          genre = { id: 123, name: "Action"}
        genre_name = genre["name"] # Pull out just the name                                         genre_name = "Action"
        genre_by_name = crud.get_genre_by_name(genre_name)  # Check if that name is in my DB        genre_by_name = (Genre object)

        # If no genre was found, then genre_by_name = None
        # If it was,             then genre_by_name = Genre(id=...., genre="Action")
        if genre_by_name == None:
            # Make a new genre
            create_genres = crud.create_genre(genre_name) # creates a new Genre object
            genre_lst.append(create_genres)
        else:
            # Add the genre that already existed to my list for this movie
            genre_lst.append(genre_by_name) # add the one that already exists in the DB

    model.db.session.add_all(genre_lst) # <---- All genres for this movie are now in the DB!
            
                
    # Create a new movie
    #----------------------
    content_id, title, tagline, vote_average, year, poster_path = (movie["id"], 
                                                                             movie["title"], 
                                                                             movie["tagline"], 
                                                                             movie["vote_average"], 
                                                                             movie["release_date"], 
                                                                             movie["poster_path"])

    db_movie = crud.create_movies(content_id, title, tagline, vote_average, year, "movies", poster_path)

    movies_in_db.append(db_movie)

    # ------------------------
    # For each Genre that we created before, create a Media_Genre linking it to this movie
    for individual_genre in genre_lst:
        print(genre_lst, db_movie.title)
        create_media = crud.create_media_genre(db_movie, individual_genre)
        model.db.session.add(create_media)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

#Open movies.json and read then process
#as looking through for each movie iterrate
    #check if genre data
        #create instance using that
        #commit to db
    #create movie instance aswell
    #commit to db
    #look through genres
        #for genres create media_genres entries
        #commit to db