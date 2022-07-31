from requests import request


API_KEY = "0fb5d9190b5e409ab1e6ad41b9bffabc"


def main():
    response = request.get(
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
    print(response.json())


main()
