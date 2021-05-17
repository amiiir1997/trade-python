import define
import requests


def update_data(symbol ,nextcall,data , timestamp , nextcallbig , databig , nextcallsmall , datasmall):

	x52= 2 / 27
	x24= 2 / 13
	x18= 2 / 10

	if(timestamp > nextcallsmall) and 0:
		i = 0
		while i == 0:
			try:
				result =requests.get('https://fapi.binance.com/fapi/v1/klines',{'symbol' : symbol , 'interval' : define.intervalsmall , 'limit' : 2}).json()
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i = 0

		datasmall[define.smallbigmadata][datasmall[define.smallbigmaindex]] = float(result[0][4])
		datasmall[define.smallbigmaindex] = (datasmall[define.smallbigmaindex] +1) % define.smallbigmacount
		datasmall[define.smallsmallmadata][datasmall[define.smallsmallmaindex]] = float(result[0][4])
		datasmall[define.smallsmallmaindex] = (datasmall[define.smallsmallmaindex] +1) % define.smallsmallmacount
		datasmall[define.smallsmallma][0] = datasmall[define.smallsmallma][1]
		datasmall[define.smallsmallma][1] = datasmall[define.smallsmallma][2]
		datasmall[define.smallsmallma][2] = datasmall[define.smallsmallma][3]
		datasmall[define.smallsmallma][3] = sum(datasmall[define.smallsmallmadata]) / define.smallsmallmacount
		datasmall[define.smallsmallmaramp] = (datasmall[define.smallsmallma][3]-datasmall[define.smallsmallma][2]) * 3 +(datasmall[define.smallsmallma][3] - datasmall[define.smallsmallma][1]) + (datasmall[define.smallsmallma][3] - datasmall[define.smallsmallma][0])/3
		datasmall[define.smallbigma][0] = datasmall[define.smallbigma][1]
		datasmall[define.smallbigma][1] = datasmall[define.smallbigma][2]
		datasmall[define.smallbigma][2] = datasmall[define.smallbigma][3]
		datasmall[define.smallbigma][3] = sum(datasmall[define.smallbigmadata]) / define.smallbigmacount
		datasmall[define.smallbigmaramp] = (datasmall[define.smallbigma][3]-datasmall[define.smallbigma][2]) * 3 +(datasmall[define.smallbigma][3] - datasmall[define.smallbigma][1]) + (datasmall[define.smallbigma][3] - datasmall[define.smallbigma][0])/3
		nextcallsmall = result[1][6] +1
		print('small data updated')



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

		data[define.ema52] = data[define.ema52]*(1-x52) + float(result[0][4])*x52
		data[define.ema24] = data[define.ema24]*(1-x24) + float(result[0][4])*x24
		data[define.signal18] = data[define.signal18]*(1-x18) + (data[define.ema24]-data[define.ema52])*x18
		data[define.macd][0] = data[define.macd][1] 
		data[define.macd][1] = data[define.macd][2] 
		data[define.macd][2] = data[define.macd][3] 
		data[define.macd][3] = data[define.ema24]-data[define.ema52]
		data[define.lastramp] = data[define.ramp]
		data[define.price] = float(result[0][4])
		data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3
		data[define.hostogramhistory][0] = data[define.hostogramhistory][1]
		data[define.hostogramhistory][1] = data[define.hostogramhistory][2]
		data[define.hostogramhistory][2] = data[define.hostogramhistory][3]
		data[define.hostogramhistory][3] = data[define.ema24] - data[define.ema52] - data[define.signal18]

		data[define.bigmadata][data[define.bigmaindex]] = float(result[i][4])
		data[define.bigmaindex] = (data[define.bigmaindex] +1) % define.bigmacount
		data[define.smallmadata][data[define.smallmaindex]] = float(result[i][4])
		data[define.smallmaindex] = (data[define.smallmaindex] +1) % define.smallmacount
		data[define.smallma] = sum( data[define.smallmadata]) / define.smallmacount
		data[define.bigma] = sum( data[define.bigmadata]) / define.bigmacount
		nextcall = result[1][6] +1
		nextcallsmall = result[1][6] +1
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


		databig[define.bigema52] = databig[define.bigema52]*(1-x52) + float(result[0][4])*x52
		databig[define.bigema24] = databig[define.bigema24]*(1-x24) + float(result[0][4])*x24
		databig[define.bigsignal18] = databig[define.bigsignal18]*(1-x18) +  (databig[define.bigema24] - databig[define.bigema52])*x18
		databig[define.bigtwolasthistogram] =databig[define.biglasthistogram] 
		databig[define.biglasthistogram] = databig[define.bighistogram]
		databig[define.bighistogram] = databig[define.bigema24] - databig[define.bigema52] - databig[define.bigsignal18]
		databig[define.bigmacddata][0] =databig[define.bigmacddata][1]
		databig[define.bigmacddata][1] =databig[define.bigmacddata][2]
		databig[define.bigmacddata][2] =databig[define.bigmacddata][3]
		databig[define.bigmacddata][3] = databig[define.bigema24] - databig[define.bigema52]
		databig[define.bigmacdramp] = (databig[define.bigmacddata][3] - databig[define.bigmacddata][2]) * 3 + (databig[define.bigmacddata][3] - databig[define.bigmacddata][1]) + (databig[define.bigmacddata][3] - databig[define.bigmacddata][0]) / 3
		databig[define.bigsignaldata][0] = databig[define.bigsignaldata][1]
		databig[define.bigsignaldata][1] = databig[define.bigsignaldata][2]
		databig[define.bigsignaldata][2] = databig[define.bigsignaldata][3]
		databig[define.bigsignaldata][3] = databig[define.bigsignal18]
		databig[define.bigsignalramp] = (databig[define.bigsignaldata][3] - databig[define.bigsignaldata][2]) * 3 + (databig[define.bigsignaldata][3] - databig[define.bigsignaldata][1]) + (databig[define.bigsignaldata][3] - databig[define.bigsignaldata][0]) / 3
		nextcallbig = result[1][6] +1
		print('big data updated')


	return [data , nextcall , databig , nextcallbig , datasmall , nextcallsmall]




