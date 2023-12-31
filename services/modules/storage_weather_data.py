
from .app_errors import error_handler
from .action_with_storage import write_new_data_to_storage
from .action_with_storage import read_all_data_from_storage
from services.files import interface_text
from services.app_classes.weather_info import WeatherInformation


@error_handler
def remembering_data_weather(weather_data_to_history: WeatherInformation) -> None:
    existing_data = read_all_data_from_storage()
    existing_data[str(len(existing_data) + 1)] = weather_data_to_history.to_dict()
    write_new_data_to_storage(existing_data)


def delete_request_history() -> None:
    empty_dictionary = {}
    write_new_data_to_storage(empty_dictionary)
    print(interface_text.ALL_REMOVED)
