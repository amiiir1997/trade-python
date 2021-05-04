import define
import requests


def update_data(symbol ,data , timestamp , nextcallbig , databig):
	i = 0
	while i == 0:
		try:
			result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalsmall , 'limit' : 2}).json()
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0


	x52= 2 / 53
	x24= 2 / 25
	x18= 2 / 19

	data[define.ema52] = data[define.ema52]*(1-x52) + float(result[0][4])*x52
	data[define.ema24] = data[define.ema24]*(1-x24) + float(result[0][4])*x24
	nextcall = result[1][6]+1
	data[define.signal18] = data[define.signal18]*(1-x18) +( data[define.ema24] - data[define.ema52] )*x18
	data[define.macd][0] = data[define.macd][1] 
	data[define.macd][1] = data[define.macd][2] 
	data[define.macd][2] = data[define.macd][3] 
	data[define.macd][3] = data[define.ema24]-data[define.ema52]
	data[define.price] = float(result[1][4])
	data[define.lastramp] = data[define.ramp]
	data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3

	if (timestamp > nextcallbig + 90):
		i = 0
		while i == 0:
			try:
				result =requests.get('https://testnet.binancefuture.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalbig , 'limit' : 2}).json()
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i = 0

		databig[define.bigema52] = databig[define.bigema52]*(1-x52) + float(result[0][4])*x52
		databig[define.bigema24] = databig[define.bigema24]*(1-x24) + float(result[0][4])*x24
		databig[define.bigsignal18] = databig[define.bigsignal18]*(1-x18) +  (databig[define.bigema24] - databig[define.bigema52])*x18
		databig[define.biglasthistogram] = databig[define.bighistogram]
		databig[define.bighistogram] = databig[define.bigema24] - databig[define.bigema52] - databig[define.bigsignal18]
		nextcallbig = result[1][6]+1


	return [data , nextcall , databig , nextcallbig]




