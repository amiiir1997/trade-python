import requests
import define

r = requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : "BTCUSDT" , 'interval' : '5m' , 'limit' : 500})
r = r.json()
x52= 2 / 53
ema52 = 0
for i in range (499):
    ema52 = ema52*(1-x52) + float(r[i][4])*x52
print(ema52)

