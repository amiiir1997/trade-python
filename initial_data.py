from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import define

def initial_data(symbol):
	data=[0,0,0,[0,0,0,0],0,0,0]
	request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
	i = 0
	while i == 0:
		try:
			result = request_client.get_candlestick_data(symbol=symbol, interval=CandlestickInterval.MIN5,  startTime=None, endTime=None, limit=1000)
			i = 1
		except:
			print('connection error')
			i = 0




	x52= 2 / 53
	x24= 2 / 25
	x18= 2 / 19


	for i in range (999):
		data[define.ema52] = data[define.ema52]*(1-x52) + float(result[i].close)*x52
		data[define.ema24] = data[define.ema24]*(1-x24) + float(result[i].close)*x24
		data[define.signal18] = data[define.signal18]*(1-x18) + (data[define.ema24]-data[define.ema52])*x18
		data[define.macd][0] = data[define.macd][1] 
		data[define.macd][1] = data[define.macd][2] 
		data[define.macd][2] = data[define.macd][3] 
		data[define.macd][3] = data[define.ema24]-data[define.ema52]
		data[define.lastramp] = data[define.ramp]
		data[define.price] = float(result[i].close)
		data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3

	nextcall = result[999].closeTime+1
	return [data , nextcall]
