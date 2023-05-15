import requests
user_city = input("Enter a city: ")
user_lat = input("Enter the latitude: ")
user_lon = input("Enter the longitude: ")
user_units = input("Enter a unit of choice: ")

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=f3bbd4ac9306c544cf4ed648b20a5e56")
        except:
            print("You have no connection!")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        unit_symbol = "C"
        if self.units == "imperial":
            unit_symbol = "F"
        print(f"In {user_city}, it is {self.temp}° {unit_symbol}")
        print(f"Today's High is: {self.temp_max}° {unit_symbol}")
        print(f"Today's Low is: {self.temp_min}° {unit_symbol}")

user_entry = City( user_city, user_lat, user_lon, units=user_units)
user_entry.temp_print()
