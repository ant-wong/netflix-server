import requests
import json

## CONSTRUCTOR
class Movie:
    def __init__(self, id, imdbid, title, image, runtime, released, synopsis, type, date):
        self.id = id
        self.imdbid = imdbid
        self.title = title
        self.image = image
        self.runtime = runtime
        self.released = released
        self.synopsis = synopsis
        self.type = type
        self.date = date


## API 
# Base URL + Headers for all calls made to uNoGS

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "ffa54bdafemshc9e17c72cee4a50p1d5db2jsn095ad383bdaa"
}


## ENDPOINTS

# getNewContent and getExpiringContent takes in 2 arguements: 
# 'country' of the requested Netflix content
# 'action' ie. GET, POST, DELETE.

def getNewContent(country, action):
  newquerystring = {"q": "{}:new7:{}".format(action, country), "p": "1", "t": "ns", "st": "adv"}
  response = requests.request("GET", url, headers=headers, params=newquerystring).json()
  
  movie_dict = {
    "ITEMS": []
  }

  for movie in response['ITEMS']:
    new_movie_obj = Movie(movie['netflixid'], movie['imdbid'], movie['title'], movie['image'], movie['runtime'], movie['released'], movie['synopsis'], movie['type'], movie['unogsdate'])
    movie_json = json.dumps(new_movie_obj.__dict__)
    movie_dict['ITEMS'].append(movie_json)
  return movie_dict

def getExpiringContent(country, action):
  expquerystring = {"q": "{}:exp:{}".format(action, country), "t": "ns", "st": "adv", "p": "1"}
  response = requests.request("GET", url, headers=headers, params=expquerystring).json()

  movie_dict = {
      "ITEMS": []
  }

  for movie in response['ITEMS']:
    new_movie_obj = Movie(movie['netflixid'], movie['imdbid'], movie['title'], movie['image'], movie['runtime'], movie['released'], movie['synopsis'], movie['type'], movie['unogsdate'])
    movie_json = json.dumps(new_movie_obj.__dict__)
    movie_dict['ITEMS'].append(movie_json)
  return movie_dict

  
