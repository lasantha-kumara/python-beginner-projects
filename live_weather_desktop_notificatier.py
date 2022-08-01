import requests
import notify2

API_KEY = "b79d7a8fdab2aa98e5ff768a7872dc30"


def main():
    # get current geo location using open weather geo location api
    city_name = "yattogoda".title()
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}")
    location_data = response.json()

    latitude = location_data[0]["lat"]
    longitude = location_data[0]["lon"]

    # get weather data of current location using open weather api
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric")
    weather_data = response.json()
    print(weather_data)

    # show current weather notification
    notify2.init("Weather notification app")

    # weather_condition = weather_data["weather"]["main"]
    # temp = weather_data["main"]["temp"]
    # message = f"Current temperature in {city_name} is {temp} and it"

    notification = notify2.Notification("Weather update", )
    notification.show()


main()
