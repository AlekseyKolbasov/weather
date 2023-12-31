
import geocoder
import requests
from http import HTTPStatus
from .process_weather_data import processing_weather_data
from .app_errors import error_handler
from .app_errors import (ApiRequestError, MissCityError, LostConnectionError)
from services.files import settings, interface_text
from ..app_classes.weather_info import WeatherInformation
 

def print_weather_data_in_my_location() -> None:
    city_name = get_current_city()
    weather_data = get_weather(city_name)
    if weather_data is not None:
        print(weather_data)


@error_handler
def print_weather_data_in_city() -> None:
    city_name = input(interface_text.ENTER_CITY).strip()
    weather_data = get_weather(city_name)
    if weather_data is not None:
        print(weather_data)


@error_handler
def get_weather(location: str) -> WeatherInformation:
    api_url = settings.API_GET_REQUEST_CITY_WEATHER.format(location=location, api_key=settings.API_KEY)
    response = requests.get(api_url)
    try:
        response.raise_for_status()
        data = response.json()
        weather_data = processing_weather_data(data)
        return weather_data
    except requests.exceptions.HTTPError:
        if (
            response.status_code == HTTPStatus.NOT_FOUND or
            response.status_code == HTTPStatus.BAD_REQUEST
        ):
            raise MissCityError
        elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            raise ApiRequestError
    except requests.exceptions.ConnectionError:
        raise LostConnectionError


def get_current_city() -> str:
    return geocoder.ip('me').city
