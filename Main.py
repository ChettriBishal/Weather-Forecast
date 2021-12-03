import requests
import configparser
from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.route('/')
def dashboard():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
	zip_code = request.form['zipCode']
	return "PIN CODE: " + zip_code

if __name__ == '__main__':
	app.debug = True
	app.run()

def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
	api_url = "http://api.openweathermap.org/data/2.5/weather?zip={},in&appid={}".format(zip_code, api_key)
	print(api_url)

get_weather_results("737102", get_api_key())