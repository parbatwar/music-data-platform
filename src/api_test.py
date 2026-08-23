import json
import requests

print("Music data ingestion started")

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)

data = response.json()

with open("data/raw/posts.json", "w") as file:
    json.dump(data, file)

print("Raw data saved.")
