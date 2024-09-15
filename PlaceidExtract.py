import json 

with open ("data.json", 'r')as f:
    data=json.load(f)

position = []
title = []
place_id = []
latitude = []
longitude = []
rating = []
reviews = []
type = []
types = []

for i in range(0,20):
    position.append(data["local_results"][i]['position'])
    title.append(data["local_results"][i]['title'])
    place_id.append(data["local_results"][i]['place_id'])
    latitude.append( data["local_results"][i]['gps_coordinates']['latitude'])
    longitude.append( data["local_results"][i]['gps_coordinates']['longitude'])
    rating.append(data["local_results"][i]['rating'])
    reviews.append(data["local_results"][i]['reviews'])
    type.append(data["local_results"][i]['type'])
    types.append(data["local_results"][i]['types'])

print(position)
print(title)
print(place_id)
print(latitude)
print(longitude)
print(rating)
print(reviews)
print(type)
print(types)    
print("=========================================")