import requests
API_KEY = "YOUR_API_KEY_HERE" #trynna be smart huh you wont find any api keys here dawg
API_KEY2= "YOUR_API_KEY_HERE" #its the fact that you even looked at this line after the first one LOL

def get_weather(city_name, country_code = 'PK'):
    geo_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}&units=metric"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    # Handle errors
    if str(geo_data.get("cod")) != "200":  # cod can be int or string
        return f"ERROR: {geo_data.get('message', 'Invalid city name')}"

    
    lat= geo_data["coord"]["lat"]
    lon= geo_data["coord"]["lon"]
    
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY2}&units=metric"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    print("Weather data api response: ", weather_data)
    temp = weather_data.get("current", {}).get("temp")
    timezone = weather_data.get("timezone", None)
    description = weather_data["current"]["weather"][0]["description"]
    return f"The current temperature in {city_input} in {timezone} is: {description} and {temp}°C" if temp is not None else "ERROR: Temperature data not found."
    
city_input = input("Enter your city name:")
print(get_weather(city_input))