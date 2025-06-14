import requests
news_response = requests.get("http://127.0.0.1:8000/get-news")

if news_response.status_code == 200:
    data = news_response.json()

    # Step 2: Send to webhook
    webhook_url = "http://127.0.0.1:8002/webhook"
    r = requests.post(webhook_url, json=data, headers={'Content-Type': 'application/json'})

    print(f"Webhook response: {r.status_code}, {r.text}")
else:
    print("Failed to fetch news.")