import serpapi
import os
from dotenv import load_dotenv
load_dotenv()

api_key= os.getenv('SERPAPI_KEY')
client=serpapi.Client(api_key=api_key)


results = client.search({
    'engine':'google_maps',
    'type':'search',
    'q':'temples in pune',
    'll':'@18.516726,73.856255,10z',
    'start':20
})

print(results)

# wwgvkjhug