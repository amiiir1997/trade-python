import requests



result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : "BTCUSDT" , 'interval' : '5m' , 'limit' : 1000}).json()

x52 = 2/53
ema52 = 0


for i in range (999):
	ema52 = ema52 * (1-x52) + float(result[i][4]) * x52

print (result[1][4])
print (ema52)
