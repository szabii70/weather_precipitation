import requests
import json
from datetime import datetime 

class WeatherDataManager():

    

    def __init__(self):
        #This prewritten data is an example, if enoigh time passed, this should be overwritten
        self.precipitation_cache = {'london': {'date_time' : datetime(2023,8,1,10,50,10), 'precipitation_data' : [1,2,3,4]}}
        self.api_key = '72fed8af3a02dd4950e5ff70ca29eb60'
        self.lat = ''
        self.lon = ''
        self.city_name = ''
        self.limit = 1

    def get_city_input(self):
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

            if len(location_data) != 0:
                self.lat = location_data[0]['lat']
                self.lon = location_data[0]['lon']

                valid_choice = True
                break
            else:
                print('Invalid city name...')
        return user_input

    def precipitation_amount(self):
        '''
        Gives a list of 60 dictionaries where each dictionary stores data of precipitation of every minute of the next 1 hour.
        This function is based on the lat, lon and api_key attributes, if these ones are missing, it can lead to an error.
        '''
        self.weather_data_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&appid={self.api_key}'
        weather_data = self.fetch_api_synchronously(self.weather_data_url)
        try:
            weather_data_precipitation = weather_data['minutely']
            return weather_data_precipitation
        except:
            raise Exception("No weather phenomana happened...")

    def segmented_precipitation_amount(self):
        '''
        Gives the amount of precipitation of every quarter of the next hour. If the cache should be updated then the function sends
        an HTTP request, otherwise it will reuturn a cached data.
        '''
        if self.cache_update_needed():
            try:
                precipitation_list = self.precipitation_amount()
                precipitation_list_byquarter = [0,0,0,0]
                quarter_counter = 0

                for index, precipitation_dic in enumerate(precipitation_list):
                    precipitation_list_byquarter[quarter_counter] += precipitation_dic['precipitation']

                    #Every quarter of an hour is checked here. If the index is dividable by 15 it means 15 minutes passed by.
                    if index%15 == 0 and index != 0:
                        quarter_counter += 1
                self.create_new_cache_record(precipitation_list_byquarter)
                return precipitation_list_byquarter
            except:
                return [0,0,0,0]
        else:
            print('Cached data is returned')
            return self.precipitation_cache[self.city_name.lower()]['precipitation_data']

    def fetch_api_synchronously(self,url):
        res = requests.get(url)
        data = json.loads(res.text)

        return data

    def cache_update_needed(self, cache_time = 20):
        '''
        This function helps to decide if a new HTTP request is required or not. Cache_time parameter gives the interval
        for long the data should be cached so it should be an integer. If there is no record of a certain city, the function should return True
        so an HTTP request is needed. If there is already a record, then if the given time (eg. 20 min) did not pass
        it should return False otherwise True. 
        '''
        try:
            previous_date_time = self.precipitation_cache[self.city_name.lower()]['date_time']
        except:
            return True

        current_date_time = datetime.now()
        time_difference = current_date_time - previous_date_time
        time_difference_in_seconds = time_difference.total_seconds()

        if time_difference_in_seconds > int(cache_time)*60:
            return True
        else:
            return False

    def create_new_cache_record(self, precipitation_data):
        print('New record is created')
        self.precipitation_cache[self.city_name.lower()] = {'date_time' : datetime.now(), 'precipitation_data' : precipitation_data}