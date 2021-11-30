from data_manager import DataManager
from flight_search import FlightSearch

datamanager = DataManager()
flightsearch = FlightSearch()

cities = datamanager.get_cities()
print(cities)

for city_name in cities:
    city_num = cities.index(city_name)
    city_code=flightsearch.find_city_code(city=city_name)
    print(city_code)
    print(city_num)
    print(datamanager.fill_city_code(city_code,city_number=city_num))

