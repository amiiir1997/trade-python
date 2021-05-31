import key

symbolnumber = 3
symbolname=["BNBUSDT" , "ADAUSDT" , "WAVESUSDT", "XRPUSDT", "NEOUSDT" , "EOSUSDT" , "DOTUSDT" , "LINKUSDT" , "DOGEUSDT","1INCHUSDT" , "BCHUSDT" , "XLMUSDT" , "ETCUSDT" , "SXPUSDT" , 'LTCUSDT']
symbollimit = [2 , 0 , 1 , 1 , 2 , 1 , 1 , 2 , 0 , 0 , 3 , 0 , 2 , 1 , 3]
simbollimitstring = ["%.2f" , "%.0f" , "%.1f" , "%.1f" , "%.2f" , "%.1f" , "%.1f" , "%.2f" , "%.0f" , "%.0f" , "%.3f" , "%.0f" , "%.2f" , "%.1f" , "%.3f"]
symbolpricelimit = ['%.2f',"%.4f","%2.3f","%1.4f","%1.3f", "%.3f" , "%.3f" , "%.3f" , "%.6f" , "%.4f" , "%.2f", "%.5f","%.3f" , "%.4f" , "%.2f"]



ema26 = 0
ema12 = 1
signal9 = 2
price = 3
histogram = 4 
lasthistogram = 5



bigema26 = 0
bigema12 = 1
bigsignal9 =2
bighistogram = 3
biglasthistogram = 4
bigtwolasthistogram = 5


position = 0
sleep = 1
openprice = 2
highlimit = 3
lowlimit = 4
lasttraderesult = 5
intrade =6
closeprice = 7
fund = 8
quantity = 9


sell = 0
buy = 1

highlimitpercent = 0.01
lowlimitpercent = 0.015
leverage = 1
interval = '5m'
intervalbig = "30m"


api_key = key.api_key
secret_key = key.secret_key






