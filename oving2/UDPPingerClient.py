import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = "192.168.1.101"# FILL IN START		# FILL IN END
port = 12000 # FILL IN START		# FILL IN END
timeout = 1 # in seconds
 
# Create UDP client socket
# FILL IN START
clientSocket = socket(AF_INET,SOCK_DGRAM)

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description
    naa0 = time.asctime()
    naa=time.time()
    data = str(ptime)+" "+str(naa)# FILL IN START		# FILL IN END
    
    try:
    	# FILL IN START
	# Record the "sent time"
        print "Packet sent: "+str(naa0)
	# Send the UDP packet with the ping message
        clientSocket.sendto(data,(host,port))
	# Receive the server response
        msg,addr=clientSocket.recvfrom(2048)
	# Record the "received time"
        naa2=time.time()
        naa3=time.asctime()
        print "Packet received: "+str(naa3)

	# Display the server response as an output
        print msg
	# Round trip time is the difference between sent and received time
        print "tid: "+str(naa2-naa)+"s\n"
        #Added newline to make it more clear.
        
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
	#Newline to make it more clear.
        print "Request timed out.\n"
        continue

# Close the client socket
clientSocket.close()
 
