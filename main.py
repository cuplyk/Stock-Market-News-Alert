import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = os.environ.get("SID_API_KEY")
ALPHA_APIKEY = os.environ.get("TOKEN_API_KEY")
NEWS_APIKEY = os.environ.get("NEWS_API_KEY")
TWILIO_TOKEN = os.environ.get("TOKEN_TWILIO")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

def get_stock_price():
    url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK_NAME}&apikey={ALPHA_APIKEY}"
    response = requests.get(url)
    data = response.json()
    time_series = data["Time Series (Daily)"]

    # Get yesterday's and day before yesterday's closing prices
    closing_prices = [float(value["4. close"]) for key, value in time_series.items()]
    yesterday_close, day_before_yesterday_close = closing_prices[:2]

    # Calculate the percentage difference
    difference_percentage = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
    return difference_percentage

def get_news():
    news_url = f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&apiKey={NEWS_APIKEY}"
    news_response = requests.get(news_url)
    news_data = news_response.json()["articles"]
    first_three_articles = news_data[:3]
    articles_info = [(article["title"], article["description"]) for article in first_three_articles]
    return articles_info

def send_sms():
    percent_diff = get_stock_price()
    articles_info = get_news()

    if abs(percent_diff) > -1:
        up_down = "🔺" if percent_diff > 0 else "🔻"
        message_body = f"{STOCK_NAME}: {up_down} {round(abs(percent_diff), 2)}%\n\n"
        for article in articles_info:
            message_body += f"Headline: {article[0]}\nBrief: {article[1]}\n\n"

        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(message.status)

send_sms()
