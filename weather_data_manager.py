import requests
import json

class WeatherDataManager():
	def __init__(self):
		#This key is required for the API call, otherwise it will not work
		self.api_key = '72fed8af3a02dd4950e5ff70ca29eb60'
		self.lat = ''
		self.lon = ''
		self.city_name = ''
		self.limit = 1
		self.coords_bycity_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}'
		self.weather_data_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}'

	def get_valid_city_input(self):
		valid_choice = False
		while valid_choice != True:
			city_name = input('Please give the name of the city for weather information: ')
			#try:
			print(coords_bycity_url)
			#res = requests.get(coords_bycity_url)
			#location_data = json.loads(res.text)
			print(location_data)
			valid_choice = True
			break
			#except:
				#print('There is no city with this name, please try again...')
