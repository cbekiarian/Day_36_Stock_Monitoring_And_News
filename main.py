import requests
import datetime as dt
from datetime import date
from datetime import timedelta
import smtplib
import html
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

my_email = ""
password = ""
URL_1 = "https://www.alphavantage.co/query"

parameters1 ={
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "datatype" : "json",
    "apikey" : "",
}

now = dt.date.today()
YESTERDAY = str(now - timedelta(days = 1))
URl_2 = "https://newsapi.org/v2/everything"
parameters2 ={
    "q": "tesla",
    "from": YESTERDAY,
    "sortBy":"popularity" ,
    "apiKey" : ""

}





def get_news():
    print ("There is more than a 5% diff")
    url2 = requests.get(url=URl_2, params=parameters2)
    url2.raise_for_status()
    art = url2.json()
    print(art)
    art = art["articles"][:3]
    print(art)
    for article in art:
        my_bytes= article["description"].encode('utf-8')
        # if value1> value2:
        #     arrow = "🔺"
        # elif value1< value2:
        #     arrow = "🔻"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg=f"Subject: TSLA: {a}% \n\n Headline: {article["title"]} \nBrief: {my_bytes}")


url = requests.get(url= URL_1,params= parameters1)
url.raise_for_status()
url_json = url.json()
time_series = url_json["Time Series (Daily)"]
print(time_series)
now = dt.date.today()
yesterday = str(now - timedelta(days = 1))
b4_yesterday =str( now - timedelta(days = 2))

print(yesterday)
print(b4_yesterday)
value1 = time_series[yesterday]["4. close"]
value2 = time_series[b4_yesterday]["4. close"]
print(value2)
print(value1)
a = abs( float(value1)- float(value2) ) / ((  (float(value1) + float(value2)) ) /2)
print(a)
if a > 0.04:
    get_news()


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

