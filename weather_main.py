from weather_data_manager import WeatherDataManager

def main():
	wdm = WeatherDataManager()

	while True:
		if wdm.get_city_input() == 'esc' : break
		wdm.segmented_precipitation_amount()
	print('End of application')

if __name__ == '__main__':
	main()