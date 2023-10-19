import requests
from datetime import date, timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "BU3NZIQ1KAAUYQYO"
NEWS_API = "9b4e462a9cb34281bafa54c6b243dc75"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'ACf550b400ec77e3ee5d0eea84e945bcf3'
auth_token = '3b1896a7737309b846888bdf2e29ec04'


parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API

}
parameters2 = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API
}

r = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = r.json()

yesterday = date.today() - timedelta(days=1)
day_before_yesterday = date.today() - timedelta(days=2)

price1 = data["Time Series (Daily)"][str(yesterday)]["4. close"]
price2 = data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
print(price1, price2)




diff_per = (abs(float(price1) - float(price2)) / float(price1))*100
print(diff_per)
if diff_per > 0:
    diff = (float(price1) - float(price2))
    if diff > 0:
        diff_amt = f"🔺{diff_per}%"
    else:
        diff_amt = f"🔻{diff_per}%"
    response = requests.get(url=NEWS_ENDPOINT, params=parameters2)
    data2 = response.json()

    news = data2["articles"][:3]
    new_news = [f"TSLA{diff_amt}\n Headline: {item['title']}. \n Brief: {item['description']}" for item in news]
    client = Client(account_sid, auth_token)
    for i in range(len(new_news)):

        message = client.messages.create(
            body=new_news[i],

            from_='+12343199779',
            to='+919175095845'
        )
        print(message.sid)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

