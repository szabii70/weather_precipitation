import requests
import json
import requests_cache
from datetime import datetime 
from precipitation_data_model import PrecipitationDataModel

class WeatherDataManager():

    

    def __init__(self):
        requests_cache.install_cache('weather_api_cache', expire_after=1200) #20 minutes
        self.api_key = '72fed8af3a02dd4950e5ff70ca29eb60'
        self.lat = ''
        self.lon = ''
        self.city_name = ''
        self.limit = 1

    def get_cityname_from_user(self):
        '''
        The city name is being requested from the user until it gives an appropriate city name.
        '''
        valid_choice = False
        while valid_choice != True:
            user_input = input('Please give the name of the city for weather information (write "esc" to escape): ')
            if user_input.lower() == 'esc' : break

            self.city_name = user_input
            self.coords_bycity_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid={self.api_key}'
            location_data = self.fetch_api_synchronously(self.coords_bycity_url)

            if len(location_data) != 0: #If the cityname is invalid then an empty list comes as result.
                self.lat = location_data[0]['lat']
                self.lon = location_data[0]['lon']

                valid_choice = True
                break
            else:
                print('Invalid city name...')
        return user_input

    def precipitation_amount(self):
        '''
        Gives a list of 61 dictionaries where each dictionary stores data of precipitation of every minute of the next 1 hour.
        This function is based on the lat, lon and api_key attributes, if these ones are missing, it can lead to an error.
        '''
        self.weather_data_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&appid={self.api_key}'
        weather_data = self.fetch_api_synchronously(self.weather_data_url)
        try:
            weather_data_precipitation_minutely = weather_data['minutely']
            return weather_data_precipitation_minutely
        except:
            raise Exception("No weather phenomana happened...")

    def segmented_precipitation_amount(self):
        '''
        Gives the amount of precipitation of every quarter of the next hour. If the cache should be updated then the function sends
        an HTTP request, otherwise it will reuturn a cached data.
        '''
        try:
            precipitation_list = self.precipitation_amount()
            precipitation_list_byquarter = [0,0,0,0]
            quarter_counter = 0

            for index, precipitation_dic in enumerate(precipitation_list):
                precipitation_list_byquarter[quarter_counter] += precipitation_dic['precipitation']

                #Every quarter of an hour is checked here. If the index is dividable by 15 it means 15 minutes passed by.
                if index%15 == 0 and index != 0:
                    quarter_counter += 1
            return PrecipitationDataModel(self.city_name,precipitation_list_byquarter,datetime.now())
        except:
            return PrecipitationDataModel(self.city_name,[0,0,0,0],datetime.now())

    def fetch_api_synchronously(self,url):
        '''
        fetch_api_synchronously(str)

        Creates synhronous HTTP requests based on the url parameter and returns its value.
        '''
        if type(url) == str:
            res = requests.get(url)
            data = json.loads(res.text)

            return data
        else:
            raise Exception('Thic function only accepts: str!')