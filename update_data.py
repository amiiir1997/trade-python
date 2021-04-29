from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import define


def update_data(symbol ,data):
	request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
	i = 0
	while i == 0:
		try:
			result = request_client.get_candlestick_data(symbol=symbol, interval=CandlestickInterval.MIN5,
														 startTime=None, endTime=None, limit=2)
			i = 1
		except Exception as e:
			print('connection error')
			print(e)
			i = 0


	x52= 2 / 53
	x24= 2 / 25
	x18= 2 / 19

	data[define.ema52] = data[define.ema52]*(1-x52) + float(result[0].close)*x52
	data[define.ema24] = data[define.ema24]*(1-x24) + float(result[0].close)*x24
	nextcall = result[1].closeTime+1
	data[define.signal18] = data[define.signal18]*(1-x18) +( data[define.ema24] - data[define.ema52] )*x18
	data[define.macd][0] = data[define.macd][1] 
	data[define.macd][1] = data[define.macd][2] 
	data[define.macd][2] = data[define.macd][3] 
	data[define.macd][3] = data[define.ema24]-data[define.ema52]
	data[define.price] = float(result[1].close)
	data[define.lastramp] = data[define.ramp]
	data[define.ramp] = (data[define.macd][3]-data[define.macd][2])*3 + (data[define.macd][3]-data[define.macd][1]) + (data[define.macd][3]-data[define.macd][0])/3

	return [data , nextcall]




