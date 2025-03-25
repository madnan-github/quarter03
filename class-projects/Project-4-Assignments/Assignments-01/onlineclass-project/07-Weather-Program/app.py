# pip install requests

import requests

api_key = "784ade1b44c464e60841773ad7968a94"
user_input = input("Enter City: ")

try:
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")
    
    response = weather_data.json()
    
    # Check for successful response
    if response.get('cod') != 200:
        print(f"Error: {response.get('message', 'Unknown error')}")
    else:
        weather = response['weather'][0]['main']
        temp = round(response['main']['temp'])
        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}°F")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except KeyError:
    print("Error: Unexpected API response format")
except Exception as e:
    print(f"An error occurred: {e}")
