


import requests
api_key = "1093cf8fad86c42347134edd12c36773"
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

LAT = 34.052235 
#47.606209
LONG = -118.243683
#-122.332069

parameters = {
    'lat' : LAT,
    'lon': LONG,
    'appid': api_key,
    'exclude': "current,minutely,daily"
}

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
print(response.url)
data = response.json()
hourly = data['hourly']

for i in range(11):
    if hourly[i]['weather'][0]['id'] < 700:
        will_rain = True
    else:
        will_rain = False

if will_rain:
    print('Bring an umbrella')
