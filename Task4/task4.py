import requests

def get_weather(city):
    API_KEY = "40bbb3d457ba3c85574e6c937a8609ff"  # Replace with your OpenWeatherMap API Key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].capitalize()
        }
        return weather
    else:
        return {"Error": "City not found or API issue"}

def main():
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    for key, value in weather_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
