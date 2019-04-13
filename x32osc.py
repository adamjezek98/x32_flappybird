from pythonosc import udp_client
import time
import math

client = udp_client.SimpleUDPClient("192.168.100.20",10023)


def set_fader(ch, val):
    ch  = ("0"+str(ch))[-2:]
    client.send_message("/ch/"+ch+"/mix/fader",val)
    client.send_message("/ch/"+ch+"/mix/on","ON" if remapper[val] % 2 else "OFF")
    client.send_message("/ch/"+ch+"/config/color/",colors[val])
    

def set_bus(ch, val):
    ch  = ("0"+str(ch))[-2:]
    client.send_message("/bus/"+ch+"/mix/fader",val)
    client.send_message("/bus/"+ch+"/mix/on","ON" if remapper[val] % 2 else "OFF")
    client.send_message("/bus/"+ch+"/config/color",colors[val])


    


def get_sin_fader(f):
    
    deg = -90 + (f * (90/8))
    val = abs(int(1024 * (math.sin(math.radians(deg)))))
    #print(c, f, deg, val)
    return val

colors = {0:"OFF",199:"RD",391:"GN",568:"YE",724:"BL",851:"MG",946:"CY",1004:"WH",1024:"OFFi"}
remapper = {0:0,199:1,391:2,568:3,724:4,851:5,946:6,1004:7,1024:8}

    
    
a = 0

vals = set()
while 1:
    a =  (a+1)%32
        
    for i in range(1,33):
        v = get_sin_fader(a+i)
        vals.add(v)
        set_fader(i,v)
        set_bus(i,v)
    time.sleep(0.1)
    #print(vals)
    




        
        


    
