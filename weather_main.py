from weather_data_manager import WeatherDataManager

def data_display(data):
	'''
	This function requires a list as a parameter. The value of the parameter is displayed on the console.
	'''
	print('\n\nThe amount of precipitation in the next 1 hour:')
	for index, value in enumerate(data):
		print(f'\t{index+1}. quarter amount: {value}')

def main():
	wdm = WeatherDataManager()

	while True:
		if wdm.get_city_input() == 'esc' : break
		precipitation_data = wdm.segmented_precipitation_amount()
		data_display(precipitation_data)
	print('End of application')

if __name__ == '__main__':
	main()