from fastapi import FastAPI
import requests

app = FastAPI()

NEWS_API_KEY = "5d9940212ce540f6a47bdb927afe03df"  # Replace with your API key

@app.get("/get-news")
def get_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {"articles": data["articles"]}
    else:
        return {"error": "Failed to fetch news", "status_code": response.status_code}

