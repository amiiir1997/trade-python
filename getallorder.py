from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import define

def getallorder ():
    request_client = RequestClient(api_key=define.api_key, secret_key=define.secret_key)
    result = request_client.get_open_orders()
    return len(result)
