import os
import requests
from requests.api import head

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        FLIGHT_SHEETY_KEY = os.environ.get("FLIGHT_SHEETY_KEY")
        self.headers={
            'Authorization': FLIGHT_SHEETY_KEY
        }
    
    def get_cities(self):
        get_cities_endpoint = "https://api.sheety.co/8b0d8b1329c1ac5cfc38d587de2306f1/flightDeals/prices"
        #headers=self.headers
        self.city_response = requests.get(url=get_cities_endpoint)
        self.city_data = self.city_response.json()
        self.cities = self.city_data['prices']
        self.cities_list = [x['city'] for x in self.cities]
        return self.cities_list

    def fill_city_code(self, city_code, city_number):
        self.city_code = city_code
        self.city_numbers = city_number + 2
        put_city_endpoint = f"https://api.sheety.co/8b0d8b1329c1ac5cfc38d587de2306f1/flightDeals/prices/{self.city_numbers}"
        params = {
            'price':{
                'iataCode': self.city_code
            }
        }
        #, headers=self.headers
        put_city_response = requests.put(url=put_city_endpoint, json=params)
        return put_city_response
