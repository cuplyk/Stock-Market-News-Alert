[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Stock-Market-News-Alert

## 🛠️ Description
This Python script fetches the latest news articles related to a given company and sends an SMS alert with the current percentage difference of a given stock's closing price compared to the previous day's closing price, along with the top three news headlines and brief descriptions.

## ⚙️  Languages or Frameworks Used
The script uses the Alpha Vantage API to fetch stock price data and the News API to fetch news articles related to the specified company.

## 🌟 How to Use
Clone this repository and navigate to the project directory.
Install the required packages using pip install -r requirements.txt.
Modify the STOCK_NAME, COMPANY_NAME, TWILIO_SID, ALPHA_APIKEY, NEWS_APIKEY, and TWILIO_TOKEN variables in the stock_alert.py script with your own values.
Run the script using python stock_alert.py.
You should receive an SMS alert with the current percentage difference of the specified stock's closing price and the top three news headlines and brief descriptions related to the specified company.
