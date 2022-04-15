import requests
import datetime as dt
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "b8f99c2d43ce4b98b27d332b45dee824"
STOCK_APIKEY = "3HS2KH8486EZAPVW"
account_sid = "AC3274fdc5ef3edf41ea8977388c8cad21"
auth_token = "e6c0ba57f1c541eb887b62d8663a4afe"


#getting yesterday and day before yesterdays date
now = dt.datetime.now()
yesterday =  (now - timedelta(1)).date()
# print(yesterday)
day_before_yesterday = (now - timedelta(2)).date()
# print(day_before_yesterday)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY
}

news_parameters = {
        "q": "tesla",
        "from": yesterday,
        "to": day_before_yesterday,
        "sortBy": "publishedAt",
        "apiKey": NEWS_APIKEY
    }

def send_news():
    res = requests.get(NEWS_ENDPOINT, news_parameters)
    res.raise_for_status()
    res = res.json()
    news_list_top3 = res["articles"][:3]
    for news in news_list_top3:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=news,
            from_="+19495233433",
            to="+917980278022"
        )
        print(message.status)



# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
url = "https://www.alphavantage.co/query"
r = requests.get(url,parameters)
r.raise_for_status()
data = r.json()
print(data)
yesterday_price = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
day_before_yesterday_price = float(data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])

#
if False:
    send_news()






 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

