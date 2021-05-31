import requests
import define

def initial_data(symbol):
	data=[0,0,0,0,0,0]
	databig = [0,0,0,0,0,0]

	
	i = 0
	while i == 0:
		try:
			result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.interval, 'limit' : 1000}).json()
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0
	i = 0
	while i == 0:
		try:
			resultbig =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalbig , 'limit' : 1000}).json()
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0



	x26= 2 / 27
	x12= 2 / 13
	x9= 2 / 10


	for i in range (999):
		data[define.ema26] = data[define.ema26]*(1-x26) + float(result[i][4])*x26
		data[define.ema12] = data[define.ema12]*(1-x12) + float(result[i][4])*x12
		data[define.signal9] = data[define.signal9]*(1-x9) + (data[define.ema12]-data[define.ema26])*x9
		data[define.price] = float(result[i][4])
		data[define.lasthistogram] = data[define.histogram]
		data[define.histogram] = data[define.ema12] - data[define.ema26] - data[define.signal9]


		databig[define.bigema26] = databig[define.bigema26]*(1-x26) + float(resultbig[i][4])*x26
		databig[define.bigema12] = databig[define.bigema12]*(1-x12) + float(resultbig[i][4])*x12
		databig[define.bigsignal9] = databig[define.bigsignal9]*(1-x9) +  (databig[define.bigema12] - databig[define.bigema26])*x9
		databig[define.bigtwolasthistogram] =databig[define.biglasthistogram] 
		databig[define.biglasthistogram] = databig[define.bighistogram]
		databig[define.bighistogram] = databig[define.bigema12] - databig[define.bigema26] - databig[define.bigsignal9]
	

	nextcall = result[999][6]+1
	nextcallbig = resultbig[999][6]+1
	return [data , nextcall, databig , nextcallbig]
