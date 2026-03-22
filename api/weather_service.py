def get_forecast(self, city, days=5):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {'q': city, 'appid': self.api_key, 'units': 'metric', 'cnt': days * 8}

    try:
        response = requests.get(forecast_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        forecast_list = []
        for forecast_data in data['list']:
            forecast_list.append(
                {
                    "date": forecast_data['dt_txt'],
                    "temp": forecast_data['main']['temp'],
                    "weather": forecast_data['weather'][0]['description'],
                }
            )
        return forecast_list
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'type': 'RequestException'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'type': type(e).__name__
        })