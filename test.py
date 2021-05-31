import define
import requests
def rsi(pricedata , index):
	up = 0
	down = 0
	for i in range (define.rsinumber-1):
		if (pricedata[(index+2+i)%define.rsinumber] - pricedata[(index + i +1) % define.rsinumber]) > 0 :
			up = up + (pricedata[(index+2+i)%define.rsinumber] - pricedata[(index + i +1) % define.rsinumber])
		else :
			down = down - (pricedata[(index+2+i)%define.rsinumber] - pricedata[(index + i +1) % define.rsinumber])
	rsi = 100 - 100 /(1+ (up / down))
	return rsi
data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : "dogeUSDT" , 'interval' : define.interval, 'limit' : 1000}).json()
index = 0
for i in range (999):
	data[index] = float(result[i][4])
	index =( index + 1)%define.rsinumber
print( rsi (data , index) )
print(index)
print(data)

