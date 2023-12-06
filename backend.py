import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()


def get_data(place, forecast_days):
    units = 'metric'
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.getenv('API_KEY')}&units={units}"
    r = requests.get(url)
    data = r.json()
    num_of_values = 8 * forecast_days
    filtered_data = data['list'][:num_of_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data('szczecin', 1))
