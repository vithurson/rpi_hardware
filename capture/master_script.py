#!/usr/bin/python
import os,sys
if(len(sys.argv)<4):
    print("usage ./master_script.py <client_id> <percentage_shared_region> <number_images_to_capture> <server_ip>(optional)")
    sys.exit(1)
if(len(sys.argv)==4):
    os.system("python sender_wrapper.py "+ " "+sys.argv[1]+" &")
else:
    os.system("python sender_wrapper.py "+ " "+sys.argv[1]+ " "+sys.argv[4]+" &")
print("waiting to establish connection")
try:
    while(~os.path.exists("con_done")):
        pass
except:
    os.system("pkill -f sender")
    os.system("pkill -f sender_")
    os.system("pkill -f th_video")
    os.system("rm running.re")
    sys.exit(0)
os.system("./run.sh 4000 400")
os.system("./th_video "+sys.argv[2]+" "+sys.argv[3]+" > /dev/null &")
try:
    while(1):
        pass
except:
    print("killing the servers")
    os.system("pkill -f sender")
    os.system("pkill -f sender_")
    os.system("pkill -f th_video")
    os.system("rm running.re")
