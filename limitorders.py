import define
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

def limitorders (symbol , lowlimitprice , highlimitprice , position , quantity,file):
	if position == "LONG":
		request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
		i=0
		while i == 0:
			try:
				highresult = request_client.post_order(symbol=symbol, side=OrderSide.SELL, ordertype=OrderType.LIMIT, closePosition=False, positionSide="BOTH" , price =highlimitprice , quantity=quantity ,timeInForce = "GTC" ,reduceOnly = 'true')
				file.write("first limitorder answer = ")
				file.write(str(highresult))
				file.write("\n")
				i=1
			except Exception as e:
				print(e)
				i=0
		i=0
		while i == 0:
			try:
				lowresult = request_client.post_order(symbol=symbol, side=OrderSide.SELL, ordertype=OrderType.STOP_MARKET, closePosition=False, positionSide="BOTH" , stopPrice =lowlimitprice , quantity=quantity , timeInForce = "GTC" , reduceOnly = 'true')
				file.write("second limitorder answer = ")
				file.write(str(lowresult))
				file.write("\n")
				i=1
			except Exception as e:
				print(e)
				i=0
	if position == "SHORT":
		request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
		i=0
		while i == 0:
			try:
				highresult = request_client.post_order(symbol=symbol, side=OrderSide.BUY, ordertype=OrderType.STOP_MARKET, closePosition=False, positionSide="BOTH" , stopPrice =highlimitprice , quantity=quantity ,timeInForce = "GTC" ,reduceOnly = 'true')
				file.write("first limitorder answer = ")
				file.write(str(highresult))
				file.write("\n")
				i=1
			except Exception as e:
				print(e)
				i=0
		i=0
		while i == 0:
			try:
				lowresult = request_client.post_order(symbol=symbol, side=OrderSide.BUY, ordertype=OrderType.LIMIT, closePosition=False, positionSide="BOTH" , price =lowlimitprice , quantity=quantity , timeInForce = "GTC" , reduceOnly = 'true')
				file.write("second limitorder answer = ")
				file.write(str(lowresult))
				file.write("\n")
				i=1
			except Exception as e:
				print(e)
				i=0
