import define

def signal(symbol ,data ,databig , position , signal, sleep , file ,initialsignal):
	file.write(str(symbol))
	file.write (' histogram = ')
	file.write(str(data[define.histogram]))
	file.write('\n')

	if data[define.histogram] < 0 and data[define.lasthistogram] > 0 and sleep == 1:
		signal = 'BUY'
		file.write ('signal buy on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0

		if databig[define.biglasthistogram]  > databig[define.bighistogram] or databig[define.bigtwolasthistogram] > databig[define.bighistogram] :
			sleep =1
			file.write ('sleep for 30min histogram')
			file.write('\n')
		if initialsignal == 1 :
			sleep =1
			file.write ('sleep for initial')
			file.write('\n')

	elif data[define.histogram] > 0 and data[define.lasthistogram] < 0 and sleep == 1:
		signal = 'SELL'
		file.write ('signal sell on ')
		file.write(str(symbol))
		file.write('\n')
		sleep = 0
		if databig[define.biglasthistogram]  < databig[define.bighistogram] or databig[define.bigtwolasthistogram] < databig[define.bighistogram] :
			sleep =1
			file.write ('sleep for 30min histogram')
			file.write('\n')
		if data[define.rsi] < 20 : 
			sleep =1
			file.write ('sleep for rsi')
			file.write('\n')


	return [ signal , sleep ]

