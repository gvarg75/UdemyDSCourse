import requests
import datetime as dt

MY_LAT = 47.6038321
MY_LONG = -122.3300624


'''iss_url = 'http://api.open-notify.org/iss-now.json'
iss_response = requests.get(url=iss_url)
iss_response.raise_for_status()

iss_data = iss_response.json()

longitude = iss_data['iss_position']['longitude']
latitude = iss_data['iss_position']['latitude']

iss_position = (longitude, latitude)
'''

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 1
}

sun_url = 'https://api.sunrise-sunset.org/json'
sun_response = requests.get(url=sun_url, params=parameters)
sun_data = sun_response.json()
sunrise = sun_data['results']['sunrise']
sunset = sun_data['results']['sunset']

print(sunrise)
print(dt.datetime.now())