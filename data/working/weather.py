import requests
import json
import os  # For file operations

# Replace with your OpenWeatherMap API key
api_key = "0ebaad5af578254aa92d49f3358377fe"

# City name (replace with your desired location)
city = "varanasi"

# File path for storing weather data (modify as needed)
data_file = "../../weather_data.json"

# Build the API request URL
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = f"{base_url}q={city}&appid={api_key}&units=metric"  # Use 'imperial' for Fahrenheit

def get_weather_data():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException:
        return None  # Indicate error

    # Parse the JSON response
    data = json.loads(response.text)
    return data


def load_saved_weather_data():
    if not os.path.exists(data_file):
        return None  # No saved data if file doesn't exist

    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except OSError:
        return None  # Indicate error


def save_weather_data(data):
    if data is None:
        return

    # Delete previous data file if it exists
    if os.path.exists(data_file):
        try:
            os.remove(data_file)
        except OSError:
            return  # Don't save if deletion fails

    # Save data to file in JSON format
    try:
        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        return


class Weather:
    @staticmethod
    def get_weather_information():
        # Try live data first
        weather_data = get_weather_data()

        # Use saved data if live retrieval fails
        if weather_data is None:
            weather_data = load_saved_weather_data()
        else:
            save_weather_data(weather_data)

        return weather_data


def print_weather_report(weather_data):
    if weather_data is None:
        return

    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]