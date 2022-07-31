import requests
import notify2

API_KEY = "b79d7a8fdab2aa98e5ff768a7872dc30"


def main():
    # get current geo location
    city_name = "yattogoda".title()
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}")
    location_data = response.json()

    latitude = location_data[0]["lat"]
    longitude = location_data[0]["lon"]

    # get weather data of current location
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}")
    weather_data = response.json()
    print(weather_data)

    # show current weather notification
    notify2.init("Weather notification app")
    notification = notify2.Notification("Weather update", )
    notification.show()


main()
