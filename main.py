import requests
import os
from datetime import datetime

USERNAME = "mukulp"
key = os.environ.get('pixkey')

pixela_endpoint = "https://pixe.la//v1/users"

user_params = {
    "token": key,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My Coding Graph",
    "Unit": "hrs",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": key
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
day = datetime.now()

pixel_config = {
    "date": day.strftime("%Y%m%d"),
    "quantity": "3.5"
}

response = requests.post(url=f"{graph_endpoint}/{graph_config['id']}", json=pixel_config, headers=headers)
print(response.text)