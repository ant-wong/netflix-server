import requests

## API
# Base URL + Headers for all calls made to DevRu

url = "https://devru-latitude-longitude-find-v1.p.rapidapi.com/latlon.php"

headers = {
    'x-rapidapi-host': "devru-latitude-longitude-find-v1.p.rapidapi.com",
    'x-rapidapi-key': "ffa54bdafemshc9e17c72cee4a50p1d5db2jsn095ad383bdaa"
}

## ENDPOINTS
# findCountry takes in 1 arguement which is a city
# eg. Vancouver, New York. (This can be lowercase OR UPPERCASE)
# The GET call then returns the country code for use.

def findCountry(location):
  querystring = {"location": "{}".format(location)}
  response = requests.request("GET", url, headers=headers, params=querystring)
  return response.text
