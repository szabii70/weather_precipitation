from weather_data_manager import WeatherDataManager

def main():
	wdm = WeatherDataManager()
	wdm.get_city_input()
	wdm.segmented_precipitation_amount()

if __name__ == '__main__':
	main()