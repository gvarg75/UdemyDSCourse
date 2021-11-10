import requests
import os
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol' : STOCK,
    'apikey' : STOCK_API_KEY,
}
stock_request = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_request.raise_for_status()
stock_data = stock_request.json()

today = datetime.datetime.now()
yesterday = str((today - datetime.timedelta(1)).date())
day_before = str((today - datetime.timedelta(2)).date())

yesterday_stock_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
day_before_stock_close = float(stock_data['Time Series (Daily)'][day_before]['4. close'])

stock_difference = yesterday_stock_close - day_before_stock_close
pct_stock_diff = (abs(stock_difference)/day_before_stock_close)*100
if stock_difference > 0:
    emoji = "⬆️"
else:
    emoji = "⬇️"

if pct_stock_diff >= 10:
    print('Get News')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
        'q': COMPANY_NAME,
        'from': day_before,
        'to': str(today.date()),
        'apiKey': NEWS_API_KEY
    }
    news_request = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    news_data = news_request.json()

    articles = news_data['articles'][:3]

    #print(articles)
    print(news_request.url)
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    account_sid = "AC45241bf273ef6ab96376d12a2a03b175"
    auth_token = os.environ.get("AUTH_TOKEN")

    for article in articles:
        headline = article['title']
        brief = article['description']

        client = Client(account_sid, auth_token)

        message = client.messages \
                    .create(
                            body=f"{STOCK}: {emoji}{pct_stock_diff}% Headline: {headline} Brief: {brief}",
                            from_='+18183909141',
                            to='+16264220999'
                        )

        print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

