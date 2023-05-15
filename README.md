# City Weather CLI Application

Introduction
This is a simple command-line interface (CLI) Python application that fetches and displays real-time weather data of a user-specified city. The weather data is retrieved from the OpenWeatherMap API.

**Features**

* Takes user input for city name, latitude, longitude, and temperature unit (Metric or Imperial)

* Fetches real-time weather data from OpenWeatherMap API

* Displays current temperature, maximum temperature, and minimum temperature

**Dependencies**

* Python 3.7+
* requests library

**How to Run**

Ensure that you have Python 3.7 or above installed on your machine.

Install requests library if not already installed. You can install it using pip:

* Copy code
* pip install requests

**Run the script in a terminal:**

* python city_weather.py
* Enter the required inputs when prompted.

**Note**

* Please make sure that you have a stable internet connection while running this application, as it fetches data from an online API. If the application cannot connect to the API, it will display a "You have no connection!" error message.
