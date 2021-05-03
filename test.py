import requests
import define

result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : "BTCUSDT" , 'interval' : define.intervalbig , 'limit' : 2}).json()



