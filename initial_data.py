import requests
import define

def initial_data(symbol):
	data=[0,0,0,[0,0,0,0],0,0,0]
	databig = [0,0,0,0,0]
	i = 0
	while i == 0:
		try:
			resultsmall =requests.get('https://testnet.binancefuture.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalsmall , 'limit' : 1000}).json()
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0
	i = 0
	while i == 0:
		try:
			resultbig =requests.get('https://testnet.binancefuture.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalbig , 'limit' : 1000}).json()
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0




	x52= 2 / 53
	x24= 2 / 25
	x18= 2 / 19


	for i in range (998):
		data[define.ema52] = data[define.ema52]*(1-x52) + float(resultsmall[i][4])*x52
		data[define.ema24] = data[define.ema24]*(1-x24) + float(resultsmall[i][4])*x24
		data[define.signal18] = data[define.signal18]*(1-x18) + (data[define.ema24]-data[define.ema52])*x18
		data[define.macd][0] = data[define.macd][1] 
		data[define.macd][1] = data[define.macd][2] 
		data[define.macd][2] = data[define.macd][3] 
		data[define.macd][3] = data[define.ema24]-data[define.ema52]
		data[define.lastramp] = data[define.ramp]
		data[define.price] = float(resultsmall[i][4])
		data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3


		databig[define.bigema52] = databig[define.bigema52]*(1-x52) + float(resultbig[i][4])*x52
		databig[define.bigema24] = databig[define.bigema24]*(1-x24) + float(resultbig[i][4])*x24
		databig[define.bigsignal18] = databig[define.bigsignal18]*(1-x18) +  (databig[define.bigema24] - databig[define.bigema52])*x18
		databig[define.biglasthistogram] = databig[define.bighistogram]
		databig[define.bighistogram] = databig[define.bigema24] - databig[define.bigema52] - databig[define.bigsignal18]


	nextcallsmall = resultsmall[999][6]+1
	nextcallbig = resultbig[999][6]+1
	return [data , nextcallsmall , databig , nextcallbig]
