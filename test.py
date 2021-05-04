import define
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *



request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.MARKET, positionSide="BOTH", quantity=0.001)
print (result.price)