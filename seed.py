import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
import requests
import time

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

#Can grab any key using this
url = "https://api.themoviedb.org/3/movie/550?api_key=496eca191c88e77e7b5701423aec44a6"

headers = {
    "accept": "application/json",
}

response = requests.get(url, headers=headers)
response_dict = response.json()

print(response_dict['title'])

data = []

for i in range(62, 562):
    url = f"https://api.themoviedb.org/3/movie/{i}?api_key=496eca191c88e77e7b5701423aec44a6"
    response = requests.get(url)
    response_dict = response.json()
    time.sleep(.2)

    if 'id' not in response_dict:
        continue
    dic = {'id': response_dict['id'],
           'title': response_dict['title'],
           'genres': response_dict['genres'],
           'tagline': response_dict['tagline'],
           'overview': response_dict['overview'],
           'runtime': response_dict['runtime'],
           'release_date': response_dict['release_date'],
           'vote_average': response_dict['vote_average'],
           'poster_path': response_dict['poster_path'],
           'original_language': response_dict['original_language'],
           'original_title': response_dict['original_title'],
           'spoken_languages': response_dict['spoken_languages'],
           }
    
    data.append(dic)

    print(dic['title'])

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

model.db.session.add_all(dic)
model.db.session.commit()