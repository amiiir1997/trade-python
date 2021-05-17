import define

def signal(symbol ,data ,databig , position , signal, sleep , file ,initialsignal ,datasmall):
	histogram = data[define.ema24] - data[define.ema52] - data[define.signal18]
	file.write(str(symbol))
	file.write (' histogram = ')
	file.write(str(histogram))
	file.write('\n')

	#if histogram > 0 and position[define.position] != "LONG":
	if data[define.hostogramhistory][0] < data[define.hostogramhistory][1] and data[define.hostogramhistory][1] < data[define.hostogramhistory][2] and data[define.hostogramhistory][2] < data[define.hostogramhistory][3] and data[define.hostogramhistory][3] - data[define.hostogramhistory][2] > data[define.hostogramhistory][2] - data[define.hostogramhistory][1] and data[define.hostogramhistory][2] - data[define.hostogramhistory][1] > data[define.hostogramhistory][1] - data[define.hostogramhistory][0]:
		signal = 'BUY'
		file.write ('signal buy on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0
		#if abs(data[define.lastramp]-data[define.ramp])/data[define.price] /3000 * 1000000 < 0.11 :
		#	sleep =1
		#	file.write ('sleep for ramp macd')
		#	file.write('\n')
		if databig[define.biglasthistogram]  > databig[define.bighistogram] or databig[define.bigtwolasthistogram] > databig[define.bighistogram] :
			sleep =1
			file.write ('sleep for 30min histogram')
			file.write('\n')
		if data[define.rsi] > 80 : 
			sleep =1
			file.write ('sleep for rsi')
			file.write('\n')
		#if initialsignal == 1 :
		#	sleep =1
		#	file.write ('sleep for initial')
		#	file.write('\n')
		#if data[define.smallma] < data[define.bigma] :
		#	sleep =1
		#	file.write ('sleep for 5min  ma')
		#	file.write('\n')
		#if databig [define.bigmacdramp] - databig [define.bigsignalramp] < 0:
		#	sleep =1
		#	file.write ('sleep for 30min macd-signal ramp')
		#	file.write('\n')
		#if datasmall[define.smallbigmaramp] > datasmall[define.smallsmallmaramp]:
		#	sleep =1
		#	file.write ('sleep for 1min ma ramp')
		#	file.write('\n')

	#elif histogram < 0 and position[define.position] != "SHORT":
	elif data[define.hostogramhistory][0] > data[define.hostogramhistory][1] and data[define.hostogramhistory][1] > data[define.hostogramhistory][2] and data[define.hostogramhistory][2] > data[define.hostogramhistory][3] and data[define.hostogramhistory][3] - data[define.hostogramhistory][2] > data[define.hostogramhistory][2] - data[define.hostogramhistory][1] and data[define.hostogramhistory][2] - data[define.hostogramhistory][1] > data[define.hostogramhistory][1] - data[define.hostogramhistory][0]:
		signal = 'SELL'
		file.write ('signal sell on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0
		#if abs(data[define.lastramp]-data[define.ramp])/data[define.price] /3000 * 1000000 < 0.11 :
		#	sleep =1
		#	file.write ('sleep for ramp macd')
		#	file.write('\n')
		if databig[define.biglasthistogram]  < databig[define.bighistogram] or databig[define.bigtwolasthistogram] < databig[define.bighistogram] :
			sleep =1
			file.write ('sleep for 30min histogram')
			file.write('\n')
		if data[define.rsi] < 20 : 
			sleep =1
			file.write ('sleep for rsi')
			file.write('\n')
		#if initialsignal == 1 :
		#	sleep =1
		#	file.write ('sleep for initial')
		#	file.write('\n')
		#if data[define.smallma] > data[define.bigma] :
		#	sleep =1
		#	file.write ('sleep for 5min ma')
		#	file.write('\n')
		#if databig [define.bigmacdramp] - databig [define.bigsignalramp] > 0:
		#	sleep =1
		#	file.write ('sleep for 30min macd-signal ramp')
		#	file.write('\n')
		#if datasmall[define.smallbigmaramp] < datasmall[define.smallsmallmaramp]:
		#	sleep =1
		#	file.write ('sleep for 1min ma ramp')
		#	file.write('\n')


	return [ signal , sleep ]

