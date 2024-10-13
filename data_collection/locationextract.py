from dotenv import load_dotenv
load_dotenv()
import serpapi
import os
import config as con
import pandas as pd




api_key = os.getenv('SERPAPI_KEY')
client=serpapi.Client(api_key=api_key)

for j in range(0,con.no_of_results,20):
    results = client.search({
        'engine':'google_maps',
        'type':'search',
        'q':con.search,
        'll':'@18.516726,73.856255,10z',
        'start':j
    })

    data = results

    position = []
    for i in range(0,20):
        position.append(data["local_results"][i]['position'])

    title = []
    for i in range(0,20):
        title.append(data["local_results"][i]['title'])

    place_id = []
    for i in range(0,20):
        place_id.append(data["local_results"][i]['place_id'])
    
    latitude = [] 
    for i in range(0,20):
        latitude.append( data["local_results"][i]['gps_coordinates']['latitude'])

    longitude = []   
    for i in range(0,20):
        longitude.append( data["local_results"][i]['gps_coordinates']['longitude'])

    rating = []      
    for i in range(0,20):
        rating.append(data["local_results"][i]['rating'])

    reviews = []       
    for i in range(0,20):
            reviews.append(data["local_results"][i]['reviews'])

    type = []    
    for i in range(0,20):
            type.append(data["local_results"][i]['type'])

    types = []    
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
    df.to_csv(f'meta_csv/meta_data_{con.search}_{j}.csv')
    print(f"{con.search}_{j}_extracted successfully")

print()
dfs = []

for j in range(0,con.no_of_results,20):
    df = pd.read_csv(f'meta_csv/meta_data_{con.search}_{j}.csv')
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(f'meta_csv/{con.search}_combined_output.csv', index=False)

print("CSV files combined successfully!")
print()
for j in range(0,con.no_of_results,20):
    os.remove(f'meta_csv/meta_data_{con.search}_{j}.csv')
    print(f'meta_data_{con.search}_{j}.csv removed successfully')