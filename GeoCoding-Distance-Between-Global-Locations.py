from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()

location_A = geolocator.geocode("NYC, NY")
location_B = geolocator.geocode("Boston, MA")

print(location_A.address)
print("... reach ...")
print(location_B.address)
#  >>>NYC, New York, United States of America
#  >>>... reach ...
#  >>>Boston, Suffolk County, Massachusetts, United States of America

NYC_NY__lat_long = (location_A.latitude, location_A.longitude)
print("...reach...")
Boston_MA__lat_long = (location_B.latitude, location_B.longitude)

print(NYC_NY__lat_long)
print(BOSTON_MA__lat_long)
#  >>>(40.7305991, -73.9865811)
#  >>>...reach...
#  >>>(42.3604823, -71.0595677)

Print(location_A.address)
Print("...reach...")
Print(location_B.address)
Print("...involves...")
print(vincenty(NYC_NY__lat_long, Boston_MA__lat_long).miles)
Print("total miles.")
#  >>>NYC, New York, United States of America
#  >>>...reach...
#  >>>Boston, Suffolk County, Massachusetts, United States of America
#  >>>...involves...
#  >>>188.875087314
#  >>>total miles.
