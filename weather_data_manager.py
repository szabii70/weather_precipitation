import requests
import json

class WeatherDataManager():

    def __init__(self):
        self.api_key = '72fed8af3a02dd4950e5ff70ca29eb60'
        self.lat = ''
        self.lon = ''
        self.city_name = ''
        self.limit = 1
        #self.weather_data_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&appid={self.api_key}'

    def get_valid_city_input(self):
        valid_choice = False
        while valid_choice != True:
            self.city_name = input('Please give the name of the city for weather information: ')
            self.coords_bycity_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid={self.api_key}'

            res = requests.get(self.coords_bycity_url)
            location_data = json.loads(res.text)

            if len(location_data) != 0:
                print(location_data[0]['lat'])
                print(location_data[0]['lon'])

                valid_choice = True
                break
            else:
                print('Invalid city name...')