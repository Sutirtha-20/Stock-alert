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


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

