import define

def signal(symbol ,data ,databig , position , signal, sleep , file ,initialsignal):
	histogram = data[define.ema24] - data[define.ema52] - data[define.signal18]
	file.write(str(symbol))
	file.write (' histogram = ')
	file.write(str(histogram))
	file.write('\n')

	if histogram > 0 and position[define.position] != "LONG":
		signal = 'BUY'
		file.write ('signal buy on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0
		if abs(data[define.lastramp]-data[define.ramp])/data[define.price] /3000 * 1000000 < 0.11 or databig[define.biglasthistogram]  > databig[define.bighistogram] or databig[define.bigtwolasthistogram] > databig[define.bighistogram]  or initialsignal == 1 or data[define.smallma] > data[define.bigma]:
			sleep =1
	elif histogram < 0 and position[define.position] != "SHORT":
		signal = 'SELL'
		file.write ('signal sell on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0
		if abs(data[define.lastramp]-data[define.ramp])/data[define.price] /3000 * 1000000 < 0.11 or databig[define.biglasthistogram]  < databig[define.bighistogram] or databig[define.bigtwolasthistogram] < databig[define.bighistogram] or initialsignal == 1 or data[define.smallma] < data[define.bigma]:
			sleep = 1



	return [ signal , sleep ]

