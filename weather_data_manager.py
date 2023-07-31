import requests
import json

class WeatherDataManager():

    def __init__(self):
        self.api_key = '72fed8af3a02dd4950e5ff70ca29eb60'
        self.lat = ''
        self.lon = ''
        self.city_name = ''
        self.limit = 1

    def get_city_input(self):
        valid_choice = False
        while valid_choice != True:
            self.city_name = input('Please give the name of the city for weather information: ')
            self.coords_bycity_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit={self.limit}&appid={self.api_key}'

            res = requests.get(self.coords_bycity_url)
            location_data = json.loads(res.text)

            if len(location_data) != 0:
                self.lat = location_data[0]['lat']
                self.lon = location_data[0]['lon']

                self.segmented_precipitation_amount()

                valid_choice = True
                break
            else:
                print('Invalid city name...')

    def precipitation_amount(self):
        '''
        Gives a list of 60 dictionaries where each dictionary stores data of precipitation of every minute of the next 1 hour.
        '''
        self.weather_data_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&appid={self.api_key}'

        res = requests.get(self.weather_data_url)
        weather_data = json.loads(res.text)
        try:
        	weather_data_precipitation = weather_data['minutely']
        	return weather_data_precipitation
        except:
        	raise Exception("No weather phenomana happened...")

    def segmented_precipitation_amount(self):
        '''
        Gives the amount of precipitation of every quarter of the next hour.
        '''
        #try:
        precipitation_list = self.precipitation_amount()
        precipitation_list_byquarter = [0,0,0,0]

        quarter_counter = 0

        for index, precipitation_dic in enumerate(precipitation_list):

            print(f'The {quarter_counter} is being summed')
            precipitation_list_byquarter[quarter_counter] += precipitation_dic['precipitation']

            if index%15 == 0 and index != 0:
                quarter_counter += 1 

        print(precipitation_list_byquarter)
        return precipitation_list_byquarter