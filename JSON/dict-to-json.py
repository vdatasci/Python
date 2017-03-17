import requests
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
data = response.json()

converted_json = json.loads(json.dumps(data))
converted_json.keys()

pretty_json = json.dumps(data, indent=1, sort_keys=True)
