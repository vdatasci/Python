import urllib, json
url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22grand%20rapids%2C%20mi%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

response = urllib.urlopen(url)

data = json.loads(response.read())

#print json.dumps(data, indent=4, sort_keys=True)

date_condition = data['query']['results']['channel']['item']['condition']['date']
temp_condition = data['query']['results']['channel']['item']['condition']['temp']
text_condition = data['query']['results']['channel']['item']['condition']['text']
