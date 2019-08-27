# Netflix Tool

### Python Flask server

#### Endpoints and what they return:

##### location.py
- Location:
```javascript
{
  "name":"New York City, New York"
  "type":"city"
  "c":"US"
  "zmw":"10001.5.99999"
  "tz":"America/New_York"
  "tzs":"EST"
  "l":"/q/zmw:10001.5.99999"
  "ll":"40.750134 -73.997009"
  "lat":"40.750134"
  "lon":"-73.997009"
}
```

##### netflix.py
- Netflix (New Content):
```javascript
{
	"download": "0",
	"image": "https://occ-0-3467-3466.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAABYKFMV0j27ILkqUbCLLW1Q_8B8ByW9ezlj8wBIZ21MxNv1lz9d6Ye1b8p_-tpUjoSRbHZO6g4jodxbQTXrDyKwJsXLtXG9s3c5MwDYuKpSnTvttLhw-L2OCXsdA.jpg?r=64a",
	"imdbid": "tt9351980",
	"largeimage": "",
	"netflixid": "81090071",
	"rating": "0",
	"released": "2019",
	"runtime": "1h50m",
	"synopsis": "In this documentary, hopes soar when a Chinese company reopens a shuttered factory in Ohio. But a culture clash threatens to shatter an American dream.<br><b>New on 2019-08-21</b>",
	"title": "American Factory",
	"type": "movie",
	"unogsdate": "2019-08-21"
}
```

- Netflix (Expiring Content):
```javascript
{
	"download": "0",
	"image": "https://occ-0-784-778.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAABUHD0xI5V2E7mcLQeGCMd5s5w-oHpdNKq0-VQRB4sD7cimGxdg07PChOesAcAb4t0mFYz3MBJ6ZWfbAvWe_ZDGjo5V62y1Y.jpg?r=b46",
	"imdbid": "tt0416044",
	"largeimage": "http://cdn0.nflximg.net/images/0478/9360478.jpg",
	"netflixid": "70075474",
	"rating": "7.3",
	"released": "2007",
	"runtime": "2h5m",
	"synopsis": "In 12th-century Asia, an orphaned slave escapes from his captors and becomes one of the greatest conquerors the world has ever known: Genghis Khan.<br><b>Expires on 2019-08-27</b>",
	"title": "Mongol",
	"type": "movie",
	"unogsdate": "2019-08-27"
}
```