import pandas as pd
import requests
import json
from datetime import datetime

df = pd.read_excel("csv.xlsx")

df = df.fillna(' ')

url = "http://127.0.0.1:8000/v1/author/"

publishers = {}
categories = {}
authors = {}


bookurl = "http://127.0.0.1:8000/v1/book/"

p = 0
c = 0
a = 0

purl = "http://127.0.0.1:8000/v1/publisher/"
curl = "http://127.0.0.1:8000/v1/category/"
aurl = "http://127.0.0.1:8000/v1/author/"


for index, row in df.iterrows():
    try:
        p = publishers[row['publisher']]
    except:
    
        temp = purl + row['publisher'].replace(" ", "+") + "/"
        res = requests.get(temp).json()
        p = res['id']
        publishers[row['publisher']] = p


    try:
        c = categories[row['category']]
    except:
        temp = curl + row['category'].replace(" ", "+") + "/"
        res = requests.get(temp).json()
        c = res['id']
        categories[row['category']] = c

    try:
        a = authors[row['authors']]
    except:
        temp = aurl + row['authors'].replace(" ", "+") + "/"
        res = requests.get(temp).json()
        a = res['id']
        authors[row['authors']] = a
        
    publishing_date = row['published_date'].strftime('%Y-%m-%d')  # Convert to string

    js = {
        "title": row['title'],
        "subtitle": row['subtitle'],
        "publishing_date": publishing_date,  # Use the converted string
        "expense": row['distribution_expense'],
        "publisher": p,
        "category": c,
        "author": a
    }
    try:
        ress = requests.post(bookurl, json=js)
    except Exception as e:
        print(e)
        print(row['title'])
        pass
  