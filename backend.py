import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()


# print(datetime.datetime.now().timestamp())


def get_data(place, forecast_days, type):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.getenv('API_KEY')}"
    r = requests.get(url)
    data = r.json()
    num_of_values = 8 * forecast_days
    filtered_data = data['list'][:num_of_values]

    # Ternary operator, I decided to use normal if/elif block
    # filtered_data = [el['main']['temp'] for el in filtered_data] if type == 'Temperature' else [el['weather'][0]['main'] for el in filtered_data]
    if type == 'Temperature':
        filtered_data = [el['main']['temp'] for el in filtered_data]
    elif type == 'Sky':
        filtered_data = [el['weather'][0]['main'] for el in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data('szczecin', 1, 'Sky'))
