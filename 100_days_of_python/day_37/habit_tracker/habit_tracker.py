import requests
import os
from datetime import datetime, timedelta

USERNAME = 'gvarg75'
TOKEN = os.environ.get("HABIT_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# #create user
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': 'habit1',
    'name': 'Running Graph',
    'unit': 'miles',
    "type": 'float',
    'color': 'ajisai'
}

headers = {
	'X-User-Token': TOKEN
	}
	
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
yesterday = today - timedelta(1)
print(yesterday)

graph_id = graph_config['id']

add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

pixel_config = {
    'date': yesterday.strftime('%Y%m%d'),
    'quantity': '10.5',
}

#add_pixel_response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
#print(add_pixel_response.text)

#update using put method
update_endpoint = f"{add_pixel_endpoint}/{yesterday.strftime('%Y%m%d')}"

update_config = {
    'quantity': '1'
}

# update_response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(update_response.text)

delete_endpoint = f"{add_pixel_endpoint}/{today.strftime('%Y%m%d')}"
delete_response = requests.delete(url=delete_endpoint, headers=headers)
print(delete_response.text)