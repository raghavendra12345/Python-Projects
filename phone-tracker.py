import phonenumbers
from phonenumbers import geocoder
import folium
import opencage
from test import number

Key="1ed0ea73100c4182abde9d7033aa0e9c"
check_num=phonenumbers.parse(number)

num_location=geocoder.description_for_number(check_num,"en")
print(num_location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(Key)

query=str(num_location)
result=geocoder.geocode(query)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng'] 

print(lat,lng)

map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup=num_location).add_to(map_location)
map_location.save("mylocation.html")

