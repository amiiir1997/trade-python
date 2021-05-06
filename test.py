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

def update(symboli , datai , timestampi ,nextcallbigi , databigi ,i):
	global data
	global nextcall
	global databig
	global nextcallbig
	[tdata , tnextcall , tdatabig , tnextcallbig] = update_data.update_data(symboli , datai ,timestampi , nextcallbigi , databigi)
	lock.acquire()
	[data[i] , nextcall , databig[i] , nextcallbig] = [tdata , tnextcall , tdatabig , tnextcallbig]
	lock.release()




for i in range(define.symbolnumber):
	[tempdata, nextcall , tempdatabig , nextcallbig] =initial_data.initial_data(define.symbolname[i])
	data.append(tempdata)
	databig.append(tempdatabig)
	position.append(["INITIAL",0,1,0,0,0,0,0,0,0])
	signal.append('NOTHING')
	sleep.append(0)
	tdata.append(threading.Thread(target = update , args =["a", 0,0 ,0 , 0] ))


fileflag = 0
orderflag = 0
print (data[0][define.smallma])
print (data[0][define.bigma])
while 1 :
	now = datetime.now()
	timestamp = datetime.timestamp(now)*1000
	if(timestamp > nextcall + 100):
		for i in range(define.symbolnumber):
			tdata[i] = threading.Thread(target = update , args =[define.symbolname[i] , data[i] ,timestamp , nextcallbig , databig[i] , i])
		for i in range(define.symbolnumber):
			tdata[i].start()
		for i in range(define.symbolnumber):
			tdata[i].join()
		print (data[0][define.smallma])
		print (data[0][define.bigma])
	time.sleep(0.5)