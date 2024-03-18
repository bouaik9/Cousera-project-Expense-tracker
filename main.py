import pandas as pd
import requests
import json

df = pd.read_excel("csv.xlsx")

categories = df['authors'].tolist()

# Filter out NaN values
categories = [category for category in categories if not pd.isna(category)]

# Remove duplicates
categories = list(set(categories))

url = "http://127.0.0.1:8000/v1/author/"

i = 0
while i < len(categories):
    batch = categories[i:i+50]  # Select a batch of categories
    lis = []
    for ele in batch:
        lis.append({"name": ele})

    res = requests.post(url, json=lis)    
    print(res.text)
    i += 50  # Move to the next batch

