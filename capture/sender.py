import os,sys
from time import sleep
import socket
from time import time
file1='test.avi'
file2='test2.avi'
syn='synch.txt'
try:
    dur = os.path.getmtime(file1)
    dur2 = os.path.getmtime(file2)
    durs = os.path.getmtime(syn)
except:
    os.system("echo > "+file1)
    os.system("echo > "+file2)
    os.system("echo > "+syn)
    dur = os.path.getmtime(file1)
    dur2 = os.path.getmtime(file2)
    durs = os.path.getmtime(syn)
count=0
las=0
las2=0
las3=0
TCP_PORT = 5000+ int(sys.argv[1])
try:
    TCP_IP = sys.argv[2]
except:
    TCP_IP = '192.168.1.148'
print("connecting to  " + TCP_IP+" at port number "+ str(TCP_PORT))
n=0
sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
print ("established connection")
os.system("echo > con_done")
def send_chuncks(data,lent):
        if(lent>0):
            size = str(len(data)).ljust(16).encode('utf-8')
            sock.send(size)
            sock.send(data)

lenss = 0
started=0
while True:
    t = time()
    if (durs != os.path.getmtime(syn)):
        durs = os.path.getmtime(syn)
        f = open(syn)
        f.seek(las3)
        l = b'3'+f.read()
        las3=f.tell()
        send_chuncks(l,len(l)) 
        f.close()
    if (dur != os.path.getmtime(file1)):
        started=1
        dur = os.path.getmtime(file1)
        f = open(file1)
        f.seek(las)
        l = b'1'+f.read()
        las=f.tell()
        send_chuncks(l,len(l)) 
        lenss+=len(l)
        f.close()
    # send shared region of image
    if (dur2 != os.path.getmtime(file2)):
        started=1
        dur2 = os.path.getmtime(file2)
        f = open(file2)
        f.seek(las2)
        l = b'2'+f.read()
        las2=f.tell()
        send_chuncks(l,len(l)) 
        lenss+=len(l)
    if(started and os.path.exists("running.re")):
        pass
    elif(started):
        print("not running")
        sock.close()
        break
    delay =0.025 - (time()-t)
    if(delay<0):
        print(delay)
        delay = 0
    sleep(delay)
