import json 
import pandas as pd


no_of_results=80

position = []
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        position.append(data["local_results"][i]['position'])


title = []
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        title.append(data["local_results"][i]['title'])

place_id = []
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        place_id.append(data["local_results"][i]['place_id'])
 
latitude = []       
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        latitude.append( data["local_results"][i]['gps_coordinates']['latitude'])

longitude = []      
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        longitude.append( data["local_results"][i]['gps_coordinates']['longitude'])

rating = []      
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        rating.append(data["local_results"][i]['rating'])

reviews = []       
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        reviews.append(data["local_results"][i]['reviews'])

type = []    
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        type.append(data["local_results"][i]['type'])

types = []    
for i in range(0,(no_of_results+1),20):
    with open (f"extracted_data\extracted_data(temples in pune)_{i}.json", 'r')as f:
        data=json.load(f)

    for i in range(0,20):
        types.append(data["local_results"][i]['types'])



data = {
    'position': position,
    'title': title,
    'place_id': place_id,
    'latitude': latitude,
    'longitude': longitude,
    'rating': rating,
    'reviews': reviews,
    'type': type,
    'types': types
}

df = pd.DataFrame(data)
     
# saving the dataframe
df.to_csv('extracted_data.csv')
print("extracted successfully")