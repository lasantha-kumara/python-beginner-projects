import requests
import notify2
import time
import datetime

API_KEY = "0fb5d9190b5e409ab1e6ad41b9bffabc"


def main():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}")
    data = response.json()
    articles = data["articles"]

    notify2.init("Tech news notification app")

    item_num = 1
    for article in articles:
        title = article['title']
        description = article["description"]

        if title == None:
            title = "Empty title"
        elif description == None:
            description = "Empty description"

        # show every titles in articles for every 10 seconds
        notification = notify2.Notification(
            f"{item_num}. {title}", description)
        notification.show()
        time.sleep(10)

        # after showing news notification add it to a txt file
        news = f"{item_num}. {title} {description}"
        today = datetime.date.today()

        with open(f"Tech news {today}.txt", "a") as file:
            file.write(news)
            file.write("\n\n")

        item_num += 1


main()
