import define
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import time
import cancelorders
import balance

def closetrade(symbol , data , position , intrade , balancemoney , file ,signal , symbolintrade):
	if signal == "BUY" and position[define.intrade] == 1:
		position[define.intrade] = 0
		position[define.intrade] = 0
		position[define.closeprice] = data[define.price]
		position[define.lasttraderesult] = (position[define.closeprice] - position[define.openprice])/position[define.openprice]
		file.write("ofline sell close on")
		file.write(str(symbol))
		file.write('\n')
		print("ofline sell close on")
		if position[define.sleep] == 0 and intrade == 1:
			symbolintrade = -1
			print (1)
			intrade = 0
			cancelorders.cancelorders(symbol , file)
			request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
			i = 0
			while i == 0:
				try:
					print (2)
					result = request_client.post_order(symbol=symbol, side=OrderSide.BUY, ordertype=OrderType.MARKET,positionSide="BOTH", reduceOnly='true',quantity=position[define.quantity])
					print (3)
					file.write("closetrade answer = ")
					file.write(str(result.json()))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0
			file.write("online sell close on")
			file.write(str(symbol))
			file.write('\n')
			i=0
			while i == 0:
				try:
					balancemoney = balance.balance()
					file.write("Balance = ")
					file.write(str(balancemoney))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0

	if signal == "SELL" and position[define.intrade] == 1:
		file.write("ofline buy close on")
		file.write(str(symbol))
		file.write('\n')
		print("ofline buy close on")
		position[define.intrade] = 0
		position[define.intrade] = 0
		position[define.closeprice] = data[define.price]
		position[define.lasttraderesult] = -1 *(position[define.closeprice] - position[define.openprice])/position[define.openprice]
		if position[define.sleep] == 0 and intrade == 1:
			symbolintrade = -1
			intrade = 0
			cancelorders.cancelorders(symbol , file)
			request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
			print (1)
			i = 0
			while i == 0:
				try:
					print(2)
					result = request_client.post_order(symbol=symbol, side=OrderSide.SELL, ordertype=OrderType.MARKET, positionSide="BOTH", reduceOnly='true',quantity=position[define.quantity])
					print (3)
					file.write("closetrade answer = ")
					file.write(str(result.json()))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0
			file.write("online buy close on")
			file.write(str(symbol))
			file.write('\n')
			i=0
			while i == 0:
				try:
					balancemoney = balance.balance()
					file.write("Balance = ")
					file.write(str(balancemoney))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0
	return [ position , intrade , balancemoney , symbolintrade]

