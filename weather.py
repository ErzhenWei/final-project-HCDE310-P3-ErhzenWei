import urllib.parse, urllib.request, json, requests
from keys import apikey
"""
This function should retrieve the real-time weather data from the MetaWeather API.
"""
def get_location_key(city_name):
    base_locations_url = "http://dataservice.accuweather.com/locations/v1/topcities/150"
    locations_url = base_locations_url + "?apikey=" + apikey
    with urllib.request.urlopen(locations_url) as location_response:
        locations = json.loads(location_response.read())
    for location in locations:
        if location["LocalizedName"] == city_name or location["EnglishName"] == city_name:
            return location["Key"]
    return None


def get_weather_data(city_name):
    try:
        base_url = 'http://dataservice.accuweather.com/currentconditions/v1/'
        location_key = get_location_key(city_name)
        weather_url = base_url + location_key + "?apikey=" + apikey
        with (urllib.request.urlopen(weather_url) as weather_response):
            data = json.loads(weather_response.read())
            print(data)
            if data:
                weather_dict = data[0]
                weather_info = [
                    weather_dict['WeatherText'],
                    weather_dict['HasPrecipitation'],
                    weather_dict['IsDayTime'],
                    weather_dict['Temperature']['Imperial']['Value']
                ]
                return weather_info
            else:
                print("No weather data available for" + city_name)
    except Exception:
        print("Error trying to retrieve data.")