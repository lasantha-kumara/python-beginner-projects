import requests
import notify2
import time


API_KEY = "0fb5d9190b5e409ab1e6ad41b9bffabc"


def main():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}")
    data = response.json()
    articles = data["articles"]

    notify2.init("News notification app")

    titles = []

    item_num = 1
    for article in articles:
        title = f"{item_num} {article['title']}\n"
        notification = notify2.Notification("Tech news today", title)
        notification.show()
        titles.append(title)
        item_num += 1
        time.sleep(5)

    print(titles)


main()
