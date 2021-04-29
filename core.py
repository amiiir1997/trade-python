import define
import signal
import closetrade
import opentrade
import update_data




def core( data ,position , signalresult , sleep ,balance , intrade ,file):
	for i in range(define.symbolnumber):
		[data[i] , nextcall]  =update_data.update_data(define.symbolname[i] , data[i])
		[signalresult[i] , sleep[i] ] = signal.signal(define.symbolname[i] , data[i] , position[i] , signalresult[i] ,sleep[i] ,file)

	for i in range(define.symbolnumber):
		if(signalresult[i] != 'NOTHING'):
			if (position[i][define.quantity] != 0):
				print('!!!!')
				[ position[i] , intrade ,balance] = closetrade.closetrade(define.symbolname[i] , data[i] , position[i] , intrade , balance,file ,signalresult[i])

	for i in range(define.symbolnumber):
		if(signalresult[i] != "NOTHING"):
			[ position[i] , intrade , balance ] = opentrade.opentrade(define.symbolname[i] , data[i] ,signalresult[i], position[i] , sleep[i],balance , intrade,file ,define.symbollimit[i] ,define.symbolpricelimit[i])
			signalresult[i] = 'NOTHING'

	return [data ,position , signalresult , sleep , intrade , nextcall]


