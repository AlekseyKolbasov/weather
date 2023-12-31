
from typing import Any

from .app_errors import error_handler
from .action_with_storage import read_all_data_from_storage

from services.files import interface_text
from services.app_classes.weather_info import WeatherInformation


@error_handler
def print_data_weather_request() -> None:
    count_of_records = int(input(interface_text.NUMBER_OF_REQUEST).strip())
    all_weather_data = read_all_data_from_storage()
    number_of_records = len(all_weather_data)
    if count_of_records < 0:
        print(interface_text.NEGATIVE_NUMBER_ENTRY)
    elif count_of_records > number_of_records:
        print_all_request_history(all_weather_data)
    else:
        print_n_last_request(count_of_records, all_weather_data)


def print_all_request_history(all_weather_data: Any) -> None:
    number_of_records = len(all_weather_data)
    print(interface_text.PRINTED_ALL_REQUESTS + str(number_of_records))
    for number_of_record in range(number_of_records, 0, -1):
        weather_data = all_weather_data[str(number_of_record)]
        weather_data_class = WeatherInformation(**weather_data)
        print(weather_data_class)


def print_n_last_request(count_of_records: int, all_weather_data: Any) -> None:
    number_of_records = len(all_weather_data)
    for number_of_record in range(number_of_records, number_of_records - count_of_records, -1):
        weather_data = all_weather_data[str(number_of_record)]
        weather_data_class = WeatherInformation(**weather_data)
        print(weather_data_class)
