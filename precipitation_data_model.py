from datetime import datetime 

class PrecipitationDataModel():
	'''
	PrecipitationDataModel(str, [int/float], datetime)
	'''

	def __init__(self, city_name, precipitation_data, date_time):
		if type(city_name) == str and type(precipitation_data) == type([]) and type(date_time) == datetime:
			self.city_name = city_name
			self.precipitation_data = precipitation_data
			self.date_time = date_time
		else:
			raise Exception('Thic class only accepts: str, [int=float], Date!')