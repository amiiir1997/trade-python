import define
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import time
import limitorders
import balance

def opentrade(symbol , data ,signal, position , sleep , balancemoney ,intrade, file ,symbollimit):
	if signal == "BUY":
		position[define.position] = "LONG"
		if(sleep == 0 and intrade== 0):
			position[define.sleep] = 0
		else:
			position[define.sleep] = 0
		position[define.intrade] = 1
		position[define.openprice] = data[define.price]
		position[define.highlimit] = data[define.price] * (1+define.highlimitpercent)
		position[define.lowlimit] = data[define.price] * (1-define.lowlimitpercent)
		position[define.quantity] = symbollimit % (balancemoney*100/100/data[define.price] * define.leverage)
		file.write("ofline buy set on")
		file.write(str(symbol))
		file.write('\n')
		if sleep == 0 and intrade == 0:
			intrade = 1
			request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
			i = 0
			while i == 0:
				try:
					result = request_client.post_order(symbol=symbol, side=OrderSide.BUY, ordertype=OrderType.MARKET, positionSide="BOTH", quantity=position[define.quantity])
					file.write("opentrade answer = ")
					file.write(str(result))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0
			limitorders.limitorders(symbol ,"%5.2f" % position[define.lowlimit] ,"%5.2f" % position[define.highlimit], "LONG" , position[define.quantity] , file)
			file.write("online buy set on")
			file.write(str(symbol))
			file.write('\n')
			i = 0
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
			

	elif signal == "SELL":
		position[define.position] = "SHORT"
		if(sleep == 0 and intrade== 0):
			position[define.sleep] = 0
		else:
			position[define.sleep] = 0
		position[define.intrade] = 1
		position[define.openprice] = data[define.price]
		position[define.highlimit] = data[define.price] * (1+define.lowlimitpercent)
		position[define.lowlimit] = data[define.price] * (1-define.highlimitpercent)
		position[define.quantity] = symbollimit % (balancemoney*(100/100)/data[define.price]* define.leverage)
		file.write("ofline sell set on")
		file.write(str(symbol))
		file.write('\n')
		if sleep == 0 and intrade == 0:
			intrade = 1
			request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
			i = 0
			while i == 0:
				try:
					result = request_client.post_order(symbol=symbol, side=OrderSide.SELL, ordertype=OrderType.MARKET, positionSide="BOTH", quantity=position[define.quantity])
					file.write("opentrade answer = ")
					file.write(str(result))
					file.write("\n")
					i = 1
				except Exception as e:
					print('connection error')
					print(e)
					i = 0
			limitorders.limitorders(symbol ,"%5.2f" % position[define.lowlimit] ,"%5.2f" % position[define.highlimit] , "SHORT" , position[define.quantity] , file)
			file.write("online sell set on")
			file.write(str(symbol))
			file.write('\n')
			i = 0
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


	return [position ,intrade, balancemoney]

