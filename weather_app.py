city = input("Enter city name: ")

weather_data = {
    "Hyderabad": "30°C, Sunny",
    "Delhi": "28°C, Cloudy",
    "Mumbai": "32°C, Humid"
}

if city in weather_data:
    print("Weather:", weather_data[city])
else:
    print("Weather data not available")
