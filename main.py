import serpapi
import os
from dotenv import load_dotenv
load_dotenv()

api_key= os.getenv('SERPAPI_KEY')
client=serpapi.Client(api_key=api_key)

results = client.search({
    'engine':'google_maps_reviews',
    'type':'search',
    'place_id':'ChIJ45xFN3rAwjsR2V37jJhvZJA'
})

print(results)