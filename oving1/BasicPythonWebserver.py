from socket import *    

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 1337

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

while True:
	print 'Ready to serve...'

	connectionSocket, addr = serverSocket.accept()
	print "Kobling fra" + str(addr)

	try:

		message =  connectionSocket.recv(1024)
		print message

		filepath = message.split()[1]
		
		f = open(filepath[1:])
		outputdata = f.read()
		print outputdata

		connectionSocket.send("\nHTTP/1.1 200 OK\r\n\r\n")
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		print "Done"
		connectionSocket.close()

	except IOError:
		connectionSocket.send("HTTP/1.1 404 File not found\r\nContent-type:text/html;charset=utf8\r\n\r\n<html><body><h1>404 File not found</h1></body></html>")		
		connectionSocket.close()

serverSocket.close()  

