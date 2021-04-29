import define
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

def cancelorders(symbol , file):
    request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
    i = 0
    while i == 0:
        try:
            result = request_client.cancel_all_orders(symbol=symbol)
            i = 1
        except:
            print('connection error')
            i = 0