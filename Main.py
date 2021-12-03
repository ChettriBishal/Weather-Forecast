import requests
import configparser
def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
	api_url = "http://api.openweathermap.org/data/2.5/weather?zip={},in&appid={}".format(zip_code, api_key)
	print(api_url)

get_weather_results("737102", get_api_key())