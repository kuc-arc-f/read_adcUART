import threading
import serial
import datetime
import time

# mDevice = "/dev/ttyACM0"
mDevice = "COM5"

mOK_CODE=1
mNG_CODE=0

# sHEAD="res_dat="

#def write(List):
def write(List  ):
	iLen =len(List)
	print("len=" + str(iLen ))
	file = open('outUART.txt','a')
	for row in List:
		#print(row)
		file.write(row)
	file.close()

def init_proc():
    from datetime import datetime
    ret_base= "000000000000000000000000"
    ser=serial.Serial(mDevice ,9600)
    #file = open('outUART.txt','w')
    #init
    file = open('outUART.txt','w')
    file.close()
    iCt=0
    List =[]
    while True:
        val=ser.readline()
        List.append(val )
        #print("IN :"  + val)
        #file.write(val)
        if (iCt >=100 ):
        	sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        	print(str(iCt) +":"+ sTime)
        	iCt=0
        	write(List )
        	List = []
        	#return
        #if (iCt >=20 ):
        #	write(List )
        #	return
        iCt=iCt +1
    #file.close()

if __name__ == "__main__":
	init_proc()
#	t = threading.Timer( 1.0, init_proc)
#	t.start() # after xx seconds, "hello, world" will be printed
