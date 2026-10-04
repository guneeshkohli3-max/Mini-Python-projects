import requests

query = input("what type of news are you interested today?\n")

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey=fd9fd6ab91e94a1894bc42e4d375f724"

r = requests.get(url)
data = r.json()

if data["status"] != "ok":

    print("ERROR:", data["message"])

else:
    articles = data["articles"]
    for index, article in enumerate(articles):
        print(index + 1, article["title"])

        print(article["url"])

        print("/n*****************************************************************/n")

        
