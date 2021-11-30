import os
import requests
import json
from datetime import datetime as dt


APP_ID = os.environ.get("NUTR_APP_ID")
APP_KEY = os.environ.get("NUTR_APP_KEY")

EXERCISE_API = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'x-remote-user-id': '0'
}

params = {
    "query":"ran 3 miles and swam 20 minutes",
}

response = requests.post(url=EXERCISE_API, headers=headers, json=params)
#print(response.json())

data = response.json()

# with open('test.json', 'w') as json_file:
#     json.dump(data, json_file)

date = dt.now().date().strftime('%Y/%m/%d')
time = dt.now().time().strftime('%H:%M:%S')

Authorization_key = os.environ.get("SHEETY_AUTH_KEY")

exercise = data['exercises']
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

headers = {
    'Authorization': Authorization_key
}

for i in range(len(exercise)):
    print(exercise[i]['user_input'])
    workout_post = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise[i]['name'],
            'duration': exercise[i]['duration_min'],
            'calories': exercise[i]['nf_calories']
        }
    }

    workout_response = requests.post(url=SHEETY_ENDPOINT, json=workout_post, headers=headers)
    print(workout_response.status_code)


