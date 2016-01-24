import time
from socket import *

host = "192.168.1.101"
port = 12000
timeout = 1

clientSocket = socket(AF_INET,SOCK_DGRAM)

clientSocket.settimeout(timeout)

ptime = 0


while ptime < 10: 
    ptime += 1
    naa0 = time.asctime()
    naa=time.time()
    data = str(ptime)+" "+str(naa)
    
    try:
        print "Packet sent: "+str(naa0)
        clientSocket.sendto(data,(host,port))
        msg,addr=clientSocket.recvfrom(2048)
        naa2=time.time()
        naa3=time.asctime()
        print "Packet received: "+str(naa3)

        print msg
        print "tid: "+str(naa2-naa)+"s\n"
        
    except:
        print "Request timed out.\n"
        continue

clientSocket.close()
 
