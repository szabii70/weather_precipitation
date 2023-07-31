from weather_data_manager import WeatherDataManager

def main():
	print("Main")
	wdm = WeatherDataManager()
	wdm.get_valid_city_input()

if __name__ == '__main__':
	main()