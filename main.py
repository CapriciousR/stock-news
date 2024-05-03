STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = ""
URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API = ""
params = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK,
    'apikey' : API_KEY,
}
new_params = {
    'q' : COMPANY_NAME,
    'apiKey' : NEWS_API,
    'sortBy' : 'relevancy',
    'pageSize' : 3
}

import requests
import datetime as dt
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

now = dt.datetime.now()


response = requests.get(url=URL, params=params)
data = response.json()['Time Series (Daily)']

data_list = [value for key,value in data.items()]

yesterday = float(data_list[3]['4. close'])
day_bef_yes = float(data_list[4]['4. close'])

if abs(day_bef_yes-yesterday) > yesterday*5/100:
    news_response = requests.get(url=NEWS_URL, params=new_params)
    news_data = news_response.json()['articles']
    diff = abs(day_bef_yes-yesterday)/yesterday *100
    if day_bef_yes < yesterday:
        up_down = "📈"
    else:
        up_down = "📉"
    for i in range(len(news_data)):    
        message = client.messages.create (
        from_='',
        to='',
        body= f"TSLA: {up_down} {round(diff)}%\nHeadline: {news_data[i]['title']} \nBrief: {news_data[i]['description']}")




