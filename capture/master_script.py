#!/usr/bin/python
import os,sys
if(len(sys.argv)<7):
    print("usage ./master_script.py <client_id> <percentage_shared_region> <number_images_to_capture> <exposure> <vblank> <shared_region_on_the_left> <downsample_scale> <server_ip> (optional)")
    sys.exit(1)
os.system("./run.sh "+sys.argv[4] +" 400")
os.system("rm -rf con_done")
if(len(sys.argv)==8):
    os.system("python sender_wrapper.py "+ " "+sys.argv[1]+" &")
else:
    os.system("python sender_wrapper.py "+ " "+sys.argv[1]+ " "+sys.argv[8]+" &")
print("waiting to establish connection")
try:
    while(not(os.path.exists("con_done"))):
        pass
except:
    os.system("pkill -f sender")
    os.system("pkill -f sender_")
    os.system("pkill -f th_video")
    os.system("rm running.re")
    sys.exit(0)
os.system("rm -rf con_done")
os.system("./th_video "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[5]+" "+sys.argv[6]+ " "+sys.argv[7]+" >log.txt")
#os.system("pkill -f sender")
#os.system("pkill -f sender_")
os.system("rm running.re")
