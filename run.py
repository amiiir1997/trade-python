from datetime import datetime
import time
import initial_data
import core
import define
import getallorder
import cancelorders
import balance
import update_data
import threading

data = []
databig = []
datasmall = []
position = []
signal = []
sleep = []
balancemoney = 0
intrade = 0
intradesymbol=-1
filetime = 0
symbolintrade = -1
file = open('log.txt' , 'w')
initialsignal = 1
tdata = []
lock = threading.Lock()


def update(symboli ,nextcalli, datai , timestampi ,nextcallbigi , databigi ,nextcallsmalli ,datasmalli , i):
	global data
	global nextcall
	global databig
	global nextcallbig
	global datasmall
	global nextcallsmall
	[tdata , tnextcall , tdatabig , tnextcallbig , tsmalldata , tnextcallsmall] = update_data.update_data(symboli ,nextcalli, datai ,timestampi , nextcallbigi , databigi , nextcallsmalli , datasmalli)
	lock.acquire()
	[data[i] , z , databig[i] , y , datasmall[i] , x] = [tdata , tnextcall , tdatabig ,tnextcallbig, tsmalldata , tnextcallsmall]
	lock.release()




for i in range(define.symbolnumber):
	[tempdata, nextcall , tempdatabig , nextcallbig , tempdatasmall , nextcallsmall] =initial_data.initial_data(define.symbolname[i])
	data.append(tempdata)
	databig.append(tempdatabig)
	datasmall.append(tempdatasmall)
	position.append(["INITIAL",0,1,0,0,0,0,0,0,0])
	signal.append('NOTHING')
	sleep.append(0)
	tdata.append(threading.Thread(target = update , args =["a", 0,0 ,0 , 0] ))


fileflag = 0
orderflag = 0
while 1 :
	now = datetime.now()
	print(now)
	timestamp = datetime.timestamp(now)*1000

	if(timestamp > nextcallsmall + 300):
		for i in range(define.symbolnumber):
			tdata[i] = threading.Thread(target = update , args =[define.symbolname[i] ,nextcall, data[i] ,timestamp , nextcallbig , databig[i] , nextcallsmall , datasmall[i] , i])
		for i in range(define.symbolnumber):
			tdata[i].start()
		for i in range(define.symbolnumber):
			tdata[i].join()
		nextcallsmall = nextcallsmall + 60000
		if(timestamp > nextcall):
			[position , signal , sleep , intrade , symbolintrade] = core.core( data , databig ,position , signal , sleep ,balancemoney , intrade ,file , symbolintrade , initialsignal , datasmall)
			nextcall = nextcall + 60000 * 5
			fileflag = 0
			orderflag = 0
			initialsignal = 0
		if(timestamp > nextcallbig):
			nextcallbig = nextcallbig + 60000 * 30
	if(timestamp > nextcall - 2000 and orderflag == 0):
		i = 0
		while i == 0:
			try :
				allorder  =  getallorder.getallorder()
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i=0
		if(allorder != 2 and intrade == 1):
			if(symbolintrade != -1):
				print("limit close")
				print(symbolintrade)
				cancelorders.cancelorders(define.symbolname[symbolintrade] , file)
				position[symbolintrade][define.sleep] = 1
				symbolintrade = -1
				intrade=0
				print("limit close")
				print(symbolintrade)


		i = 0
		while i == 0:
			try:
				balancemoney = balance.balance()
				file.write("Balance = ")
				file.write(str(balancemoney))
				file.write("\n")
				i = 1
			except Exception as e:
				print('connection error')
				print(e)
				i = 0
		orderflag = 0
	if (timestamp > nextcall - 5000 and fileflag == 0):
		file.write(str(now))
		file.write("\n")
		file.close()
		file = open('log.txt', 'a')
		fileflag = 1
	time.sleep(0.5)