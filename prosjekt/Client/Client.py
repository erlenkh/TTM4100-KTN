# -*- coding: utf-8 -*-
import socket, json, re, time
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser


#Best regex ever.
regex = re.compile(r'(\w+)?(\s)?(.*)')

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        self.host = host
        self.server_port = server_port
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.kommandoer = ['login','logout','msg','names','help']

        #What did this do again? Can't remember, but lets let it stay.
        #self.mottaker = MessageReceiver(self,self.connection)
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print "[*] Kobling etablert"
        lytter = MessageReceiver(self,self.connection)
        lytter.daemon = True
        lytter.start()
        print "[*] Lytter startet."
        self.handle_input()
        
    def disconnect(self):
        self.connection.close()

        #This shit will only work with banning/kicking cause thats how I roll.
        # TODO: Handle disconnection

    def receive_message(self, message, connection):
        parser = MessageParser()
        print parser.parse(message)

    def send_payload(self, inputen):
        payload = {}
        a = ""
        #REGEX POWAH
        if regex.search(inputen).group(3) == "": a = None
        else: a = regex.search(inputen).group(3)
        
        #Do you have a moment to talk about our lord and savior, Regex?
        payload['request'] = regex.search(inputen).group(1)
        payload['content'] = a
        payload_json = json.dumps(payload)

        self.connection.send(payload_json)


    def handle_input(self):
        a = True
        while a:
            inn_tekst = str(raw_input("> "))
            self.send_payload(inn_tekst)
            time.sleep(0.1)
    # More methods may not be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
