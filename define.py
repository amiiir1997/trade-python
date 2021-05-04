import key

symbolnumber = 14
symbolname=["BNBUSDT" , "ADAUSDT" , "WAVESUSDT", "XRPUSDT", "NEOUSDT" , "EOSUSDT" , "DOTUSDT" , "LINKUSDT" , "DOGEUSDT","1INCHUSDT" , "BCHUSDT" , "XLMUSDT" , "ETCUSDT" , "SXPU>
symbollimit = [2 , 0 , 1 , 1 , 2 , 1 , 1 , 2 , 0 , 0 , 3 , 0 , 2 , 1]
simbollimitstring = ["%.2f" , "%.0f" , "%.1f" , "%.1f" , "%.2f" , "%.1f" , "%.1f" , "%.2f" , "%.0f" , "%.0f" , "%.3f" , "%.0f" , "%.2f" , "%.1f"]
symbolpricelimit = ['%3.2f',"%1.5f","%2.4f","%1.4f","%1.3f", "%.3f" , "%.3f" , "%.3f" , "%.6f" , "%.4f" , "%.2f", "%.5f","%.3f" , "%.4f"]



ema52 = 0
ema24 = 1
signal18 = 2
macd =3
ramp = 4
lastramp = 5
price = 6

bigema52 = 0
bigema24 = 1
bigsignal18 =2
bighistogram = 3
biglasthistogram = 4


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
intervalsmall = '5m'
intervalbig = "30m"


api_key = key.api_key
secret_key = key.secret_key






