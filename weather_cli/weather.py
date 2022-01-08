import os
import requests
from requests import Response
from typing import Tuple
from .helpers import kelvin_to_fahrenheit


API_KEY = os.getenv("API_KEY", "redacted")
DEGREE_SIGN = "\N{DEGREE SIGN}"


def _base_uri(city_name: str) -> str:
    city_name = city_name.replace(" ", "")
    return (
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    )


def get_weather(city_name: str) -> Response:
    try:
        with requests.Session() as s:
            response = s.get(_base_uri(city_name))
    except:
        raise
    return response


def _build_city_url(city_id: int) -> str:
    return f"https://openweathermap.org/city/{city_id}"


def parse_response(response: dict) -> Tuple[str]:
    """
    Parse OpenWeatherMap API Response

    Sample Response:
        {'coord': {'lon': -87.65, 'lat': 41.85},
         'weather': [{'id': 801,
           'main': 'Clouds',
           'description': 'few clouds',
           'icon': '02d'}],
         'base': 'stations',
         'main': {'temp': 269.13,
          'feels_like': 266.32,
          'temp_min': 268.1,
          'temp_max': 270.05,
          'pressure': 1021,
          'humidity': 61},
         'visibility': 10000,
         'wind': {'speed': 1.79, 'deg': 212, 'gust': 3.58},
         'clouds': {'all': 22},
         'dt': 1641666312,
         'sys': {'type': 2,
          'id': 2005153,
          'country': 'US',
          'sunrise': 1641647868,
          'sunset': 1641681387},
         'timezone': -21600,
         'id': 4887398,
         'name': 'Chicago',
         'cod': 200}
    """
    lat, lon = response["coord"]["lat"], response["coord"]["lon"]
    city = response["name"]
    city_id = response["id"]
    country = response["sys"]["country"]
    weather = response["weather"][0]["main"]
    temp_min = kelvin_to_fahrenheit(response["main"]["temp_min"])
    temp_max = kelvin_to_fahrenheit(response["main"]["temp_max"])
    feels_like = kelvin_to_fahrenheit(response["main"]["feels_like"])
    humidity = response["main"]["humidity"]

    return (
        f"{city}, {country} [Lat: {lat}, Lon:{lon}]\n",
        f"Feels like {feels_like}{DEGREE_SIGN}, {weather}.\n",
        f"Low: {temp_min}{DEGREE_SIGN}",
        f"High: {temp_max}{DEGREE_SIGN}",
        f"Humidity: {humidity}%\n",
        f"{_build_city_url(city_id)}",
    )
