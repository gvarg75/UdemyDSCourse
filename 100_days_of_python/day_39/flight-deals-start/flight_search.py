import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.FLIGHT_API_KEY = os.environ.get("FLIGHT_API_KEY")
    
    def find_city_code(self, city):
        self.city = city
        city_query_endpoint = 'https://tequila-api.kiwi.com/locations/query'
        headers ={
            'apikey': self.FLIGHT_API_KEY
        }
        params= {
            'term': self.city
        }
        city_response = requests.get(url=city_query_endpoint, params=params, headers=headers).json()
        city_code = city_response["locations"][0]['code']
        
        return city_code