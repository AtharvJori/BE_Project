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

data1 = {'position': position,
'title': title,
'place_id': place_id,
'latitude': latitude,
'longitude': longitude,
'rating': rating,
'reviews': reviews,
'type': type,
'types': types}

# Writing to sample.json
with open("extracted_data.json", "w") as outfile:
	outfile.write(json.dumps(data1, indent=4))

if(outfile):
    print("extracted successfully")