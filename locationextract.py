from dotenv import load_dotenv
load_dotenv()
import serpapi
import os
import json 


no_of_results=80
search='temples in pune'



api_key = os.getenv('SERPAPI_KEY')
client=serpapi.Client(api_key=api_key)

for i in range(0,(no_of_results+1),20):
    results = client.search({
        'engine':'google_maps',
        'type':'search',
        'q':search,
        'll':'@18.516726,73.856255,10z',
        'start':i
    })


    # Use this data for testing
    # results = {'position': "hiiiiii",
    #     'title': "hiiiiii",
    #     'place_id': "hiiiiii",
    #     'latitude': "hiiiiii",
    #     'longitude': "hiiiiii",
    #     'rating': "hiiiiii",
    #     'reviews': "hiiiiii",
    #     'type': "hiiiiii",
    #     'types': "hiiiiii"}

    results = str(results)

    with open(f"extracted_data\{search}_{i}.json", "w") as outfile:
        outfile.write(results)

    if(outfile):
        print(f"extracted successfully {i}")
