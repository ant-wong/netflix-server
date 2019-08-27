import requests
import json

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
  return response

def getExpiringContent(country, action):
  expquerystring = {"q": "{}:exp:{}".format(action, country), "t": "ns", "st": "adv", "p": "1"}

  response = requests.request("GET", url, headers=headers, params=expquerystring).json()
  return response

  
