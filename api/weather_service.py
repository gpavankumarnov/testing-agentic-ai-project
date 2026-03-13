import requests
import json


class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
            }
        else:
            return None

    def get_forecast(self, city, days=5):
        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {"q": city, "appid": self.api_key, "units": "metric", "cnt": days * 8}

        # BUG1: Missing error handling for forecast API call
        response = requests.get(forecast_url, params=params)
        data = response.json()

        forecast_list = []
        for item in data["list"]:
            forecast_list.append(
                {
                    "date": item["dt_txt"],
                    "temp": item["main"]["temp"],
                    "weather": item["weather"][0]["description"],
                }
            )

        return forecast_list
