from dotenv import load_dotenv
load_dotenv()
import serpapi
import os
import config as con
import pandas as pd
import csv


reviews = []  
topics = []  
place_id = []

fn=f'location_csv/{con.search}_combined_output.csv'
cn='place_id'



api_key = os.getenv('SERPAPI_KEY')
client=serpapi.Client(api_key=api_key)


with open(fn, mode='r') as file:
    csv_reader = csv.DictReader(file)
    j = 1
    # Iterate over rows in the CSV
    for row in csv_reader:
        # Access the column by its header (column name)
        # print(row[cn])
        place_id.append(row[cn])


        #serp API code will replace below result
        result = client.search({
            'engine': "google_maps_reviews",
            'place_id': row[cn],
            'sort_by': "ratingHigh"
        })

        # print(result)

        review = []
        if(len(result["reviews"])>10):
            count = 10
        else:
            count = len(result["reviews"])

        for i in range(0,count):
            try:
                if result["reviews"][i]['extracted_snippet']:
                    review.append(result["reviews"][i]['extracted_snippet']['original'])
            except KeyError:
                print(f"No reiviews were found for {row["title"]}")
                continue
        reviews.append(review)
        
        # print(review)
        

        topic = []
        
        try:
            if result["topics"]:
                for i in range(0,len(result["topics"])):
                    topic.append(result["topics"][i]['keyword'])
                topics.append(topic)        
        except KeyError:
            print(f"No topics were found for {row["title"]}")
            topics.append("NA")        

        
        # print(topic)
        print(j)
        j = j+1
        


    data = {
        'place_id': place_id,
        'reviews': reviews,
        'topics': topics
    }

    # print(data)
    df = pd.DataFrame(data)
        
    # saving the dataframe
    df.to_csv(f'review_csv/review_{con.search}.csv')
    print(f"{con.search}_extracted successfully")
