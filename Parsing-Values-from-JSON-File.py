from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

pprint(data)


#data["maps"][0]["id"]  # will return 'blabla'
#data["masks"]["id"]    # will return 'valore'
#data["om_points"]      # will return 'value'
