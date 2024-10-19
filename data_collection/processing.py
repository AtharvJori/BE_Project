import pandas as pd
import numpy as np
import re
import ast
import nltk
from nltk.corpus import stopwords


df =pd.read_csv("review_csv/review_temples in pune.csv")

# drop the column
df = df.drop('Unnamed: 0', axis=1)

# added the position column in the df
df['Position'] = range(1, len(df) + 1)

# repositioning the columns
df = df[['Position','place_id','reviews','topics']]

# it will remove the items from the list , make it in one place
# for the topics column
df['topics'] = df['topics'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else x)
df['topics'] = df['topics'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')


# for the reviews column
df['reviews'] = df['reviews'].apply(ast.literal_eval)
df['reviews'] = df['reviews'].apply(lambda x: ', '.join(x))

# converting text to lower case
df['reviews']=df['reviews'].apply(lambda x:x.lower())
df['topics']=df['topics'].apply(lambda x:x.lower())

# removing , . / ? and other symbols
df['reviews'] = df['reviews'].str.replace(r'[,\.?\n]', '', regex=True)


# this removes emojis from the text
def remove_emojis(text):
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # geometric shapes
        "\U0001F800-\U0001F8FF"  # supplemental arrows
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U00002600-\U000026FF"  # miscellaneous symbols
        "\U00002700-\U000027BF"  # dingbats
        "\U0001FA00-\U0001FA6F"  # chess symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

df['reviews'] = df['reviews'].apply(remove_emojis)


# STop word removal
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word.lower() not in stop_words])
df['reviews'] = df['reviews'].apply(remove_stopwords)


#  this will apply stemming to the text
from  nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem(text):
    y =[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y) 

df['reviews']=df['reviews'].apply(stem)

df.to_csv(f'processed_csv/review_processed.csv')