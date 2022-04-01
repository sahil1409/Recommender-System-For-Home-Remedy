#!C:\Python37\python.exe

import cgi, cgitb, os
import geocoder

import requests
import json

# Importing required libraries
from googleplaces import GooglePlaces, types, lang
import requests
import json

print("Content-type: text/html")
print("")
print("<html><head>")
print("<title>HousedHealth</title>")
print("<link rel='stylesheet' href='CSS/Predictions.css'>")
print("<link rel='icon' href='https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/64/000000/external-hospital-medical-kiranshastry-lineal-color-kiranshastry-2.png'/>")


print("</head><body onload='getLocation()' style='background: linear-gradient(to bottom, #93a5cf 0%, #e4efe9 100%);'>")

g = geocoder.ip('me')
var = g.latlng
#print("<h1>%s %s</h1>" % (var[0], var[1]))


send_url = "http://api.ipstack.com/check?access_key=8301281bccb762990fe3328c6adc9297"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
lat = geo_json['latitude']
long = geo_json['longitude']
city = geo_json['city']

print("<h1 class='Category' style='text-align: center; color: aliceblue; font-size: 3em;'>Nearby Hospitals</h1>")

API_KEY = 'AIzaSyClmEY1sR0lgC2aXImNwGZ9TIk7z0LfsfQ'

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(
		lat_lng ={'lat': lat, 'lng': long},
		radius = 5000,
		types =[types.TYPE_HOSPITAL])

# If any attributions related
# with search results print them
if query_result.has_attributions:
	print (query_result.html_attributions)

# Iterate over the search results
for place in query_result.places:
	# print(type(place))
	# place.get_details()
    if ((("Hospital" or "HOSPITAL") in place.name) and (("Infertility" or "Maternity") not in place.name)): 
        print("<h2>%s </h2>" % (place.name))
        print()

print("</body>")
print("</html>")
