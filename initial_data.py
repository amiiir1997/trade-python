import requests
import define

def initial_data(symbol):
	data=[0,0,0,[0,0,0,0],0,0,0]
	i = 0
	while i == 0:
		try:
			result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.interval , 'limit' : 1000}).json()
			i = 1
		except:
			print('connection error')
			i = 0




	x52= 2 / 53
	x24= 2 / 25
	x18= 2 / 19


	for i in range (999):
		data[define.ema52] = data[define.ema52]*(1-x52) + float(result[i][4])*x52
		data[define.ema24] = data[define.ema24]*(1-x24) + float(result[i][4])*x24
		data[define.signal18] = data[define.signal18]*(1-x18) + (data[define.ema24]-data[define.ema52])*x18
		data[define.macd][0] = data[define.macd][1] 
		data[define.macd][1] = data[define.macd][2] 
		data[define.macd][2] = data[define.macd][3] 
		data[define.macd][3] = data[define.ema24]-data[define.ema52]
		data[define.lastramp] = data[define.ramp]
		data[define.price] = float(result[i][4])
		data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3

	nextcall = result[999][6]+1
	return [data , nextcall]
