
import requests
import json


def get_weather(city):
    # API endpoint and your OpenWeatherMap API key
    api_key = "API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()

        # Parse the weather data
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        # Convert temperature from Kelvin to Celsius
        temperature_celsius = temperature - 273.15

        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (KeyError, IndexError):
        print("Error: Failed to parse weather data.")
    except json.JSONDecodeError:
        # Print the response received from the API
        print("Error: Failed to decode weather data.")


if __name__ == '__main__':
    city = input("Enter a city name: ")
    get_weather(city)
