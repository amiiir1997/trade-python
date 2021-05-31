import define
import requests


def update_data(symbol ,nextcall,data , timestamp , nextcallbig , databig):

	x26= 2 / 27
	x12= 2 / 13
	x9= 2 / 10

	if(timestamp > nextcall):
		i = 0
		while i == 0:
			try:
				result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.interval , 'limit' : 2}).json()
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i = 0

		data[define.ema26] = data[define.ema26]*(1-x26) + float(result[0][4])*x26
		data[define.ema12] = data[define.ema12]*(1-x12) + float(result[0][4])*x12
		data[define.signal9] = data[define.signal9]*(1-x9) + (data[define.ema12]-data[define.ema26])*x9
		data[define.price] = float(result[0][4])
		data[define.lasthistogram] = data[define.histogram]
		data[define.histogram] = data[define.ema12] - data[define.ema26] - data[define.signal9]

		nextcall = result[1][6] +1
		print('data updated')



	if(timestamp > nextcallbig):
		i = 0
		while i == 0:
			try:
				result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalbig , 'limit' : 2}).json()
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i = 0


		databig[define.bigema26] = databig[define.bigema26]*(1-x26) + float(result[0][4])*x26
		databig[define.bigema12] = databig[define.bigema12]*(1-x12) + float(result[0][4])*x12
		databig[define.bigsignal9] = databig[define.bigsignal9]*(1-x9) +  (databig[define.bigema12] - databig[define.bigema26])*x9
		databig[define.bigtwolasthistogram] =databig[define.biglasthistogram] 
		databig[define.biglasthistogram] = databig[define.bighistogram]
		databig[define.bighistogram] = databig[define.bigema12] - databig[define.bigema26] - databig[define.bigsignal9]
		nextcallbig = result[1][6] +1
		print('big data updated')


	return [data , nextcall , databig , nextcallbig]




