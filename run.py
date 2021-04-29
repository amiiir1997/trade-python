from datetime import datetime
import time
import initial_data
import core
import define
import getallorder
import cancelorders
import balance

data = []
position = []
signal = []
sleep = []
balancemoney = 0
intrade = 0
intradesymbol=-1
filetime = 0
file = open('log.txt' , 'w')


for i in range(define.symbolnumber):
	[tempdata, nextcall] =initial_data.initial_data(define.symbolname[i])
	data.append(tempdata)
	position.append(["INITIAL",0,1,0,0,0,0,0,0,0])
	signal.append('NOTHING')
	sleep.append(0)


fileflag = 0
orderflag = 0
while 1 :
    now = datetime.now()
    print(now)
    timestamp = datetime.timestamp(now)*1000
    if(timestamp > nextcall):
        [ data ,position , signal , sleep , intrade ,nextcall] = core.core( data ,position , signal , sleep ,balancemoney , intrade ,file)
        fileflag = 0
        orderflag = 0
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
        if(allorder == 1):
            for i in range(define.symbolnumber):
                cancelorders.cancelorders(define.symbolname[i] , file)
            intrade=0
            #position[intradesymbol][define.intrade]=0

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