# -*- coding: utf-8 -*-
import SocketServer, re, json
from time import time, asctime, sleep
from threading import Thread
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""
messages = []
users = []
class ClientHandler(SocketServer.BaseRequestHandler):
    global messages
    global users
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.kommandoer = ['login','logout','msg','names','help','history']
        self.messageCount = 0
        self.loggedin = 0
        self.username = ""
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        #this shit so guuuud
        handleUpdates = Thread(target=self.update_clients)
        handleUpdates.setDaemon = True
        handleUpdates.start()

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            print "[*] Mottat: "+str(received_string)

            recv = json.loads(received_string)

            request = recv['request']
            content = recv['content']
            
            if request == 'login':
                self.handle_login(content)
            elif request == 'logout':
                self.handle_logout()
            elif request == 'msg':
                self.handle_msg(content)
            elif request == 'names':
                self.handle_names()
            elif request == 'help':
                self.handle_help()
            elif request == 'history':
                self.handle_history()
            else:
               self.handle_error()

    #best function 2016 for president:
    def update_clients(self):
        while True:
            sleep(0.5) #delay så servern kan chilln litt.
            if self.messageCount < len(messages) and self.messageCount>0: #=> time to update this bitch.
                for i in range(self.messageCount,len(messages)):
                    self.connection.sendall(messages[i])
                    self.messageCount += 1



    #boring functions be down here.
    def handle_login(self,user):
        if not user:
            self.handle_error()
            return
        if user and re.search('[A-Za-z0-9]+',user) == False:
            self.handle_error()
            return

        if self.loggedin == 1:
            self.handle_error()
            return

        if user not in users:
            self.username = user
            users.append(user)
            self.loggedin = 1
            payload = {'timestamp':asctime(),'sender':'server','response':'info','content':'User logged in.'}
            self.send(payload)


    def handle_logout(self):
        if self.loggedin==0:
            self.handle_error()
        else:
            self.loggedin = 0
            temp = self.username
            users.remove(self.username)
            payload = {'timestamp':asctime(),'sender':temp,'response':'info','content':'Logged out.'}
            self.send(payload)

    def handle_msg(self,message):
        if not message:
            self.handle_error()
        elif self.loggedin == 0:
            self.handle_error()
        else:
            messages.append(asctime()+":"+self.username+": "+message)
            payload = {'timestamp':asctime(),'sender':'test','response':'message','content':message}
            self.send(payload)

    def handle_names(self):
        if self.loggedin == 0:
            self.handle_error()
            return
        content = ""
        for i in range(len(users)):
            content+=users[i]+", "
        payload = {'timestamp':asctime(),'sender':'server','response':'info','content':content}
        self.send(payload)


    def handle_history(self):
        if self.loggedin == 0:
            self.handle_error()
            return
        content = ""
        for i in range(len(messages)):
            content += messages[i]+"\n"
        payload = {'timestamp':asctime(),'sender':'server','response':'history','content':content}
        self.send(payload)



    def handle_error(self):
        timestamp = asctime()
        tsascii = asctime() #mulig at jeg bruker denne senere.
        payload = {'timestamp':tsascii,'sender':'server','response':'error','content':'Invalid command.'}
        self.send(payload)


    def handle_help(self):
        content = "Help: Commands: Login, Logout, msg, names, history. Usage: command + content"
        payload = {'timestamp':asctime(),'sender':'server','response':'info','content':content}
        self.send(payload)

    def send(self,data):
        self.request.sendall(json.dumps(data))

        # TODO: Add handling of received payload from client



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print '[*] Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
