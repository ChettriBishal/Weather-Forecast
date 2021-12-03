import requests

def get_weather_results(zip_code, api_key):
	api_url = "http://api.openweathermap.org/data/2.5/weather?zip={},in&appid={}".format(zip_code, api_key)
	print(api_url)

get_weather_results("737102", "7093782ef452f0ded971c54a2f343a2d")