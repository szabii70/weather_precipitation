from weather_data_manager import WeatherDataManager
from data_exporter import DataExporter

wdm = WeatherDataManager()
exporter = DataExporter()

def precipitation_data_display(data):
	'''
	This function requires a PrecipitationDataModel as a parameter. Its attributes will be displayed.
	'''
	print(f'\n\nIn {data.city_name.title()} from {data.date_time.strftime("%m/%d/%Y, %H:%M:%S")} the amount of precipitation in the next 1 hour:')
	for index, value in enumerate(data.precipitation_data):
		print(f'\t{index+1}. quarter amount: {value} mm/h')
	print('\n\n')

def main():

	while True:
		if wdm.get_cityname_from_user() == 'esc' : break
		precipitation_data_model = wdm.segmented_precipitation_amount()
		exporter.export_precipitation_datamodel_to_csv(precipitation_data_model, 'PrecipitationData.csv')
		precipitation_data_display(precipitation_data_model)
	print('End of application')

if __name__ == '__main__':
	main()