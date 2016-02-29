# -*- coding: utf-8 -*-
import socket, json, re, time
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

regex = re.compile(r'(.*) ?(.*)',re.M | re.I)

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

        #self.mottaker = MessageReceiver(self,self.connection)

        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print "[*] Kobling etablert"
        lytter = MessageReciver(client,self.connection)
        lytter.daemon = True
        lytter.start()
        print "[*] Lytter startet."
        
    def disconnect(self):
        self.connection.close()
        # TODO: Handle disconnection

    def receive_message(self, message, connection):
        parser = MessageParser()
        print parser.parse(message)

    def send_payload(self, kommandoen, melding):
        # TODO: Handle sending of a payload
        payload = {}

        payload['request'] = kommandoen
        payload['content'] = melding
        payload_json = json.dumps(payload)

        self.connection.send(payload_json)


    def handle_input(self):
        a = True
        while a:
            inn_tekst = str(input("> "))
            kommando = regex.search(inn.tekst).group(1)
            if len(regex.search(inn_tekst).group().split(" ")) != 1 or len(regex.search(inn_tekst).group().split(" ")) != 2:
                print "[*] Error: Ugyldig input."
            elif kommando == 'logout':
                self.disconnect()
            elif kommando in kommandoer:
                self.send_payload(kommando,regex.search(inn_tekst).group(2))
                #a = False
            else:
                print "[*] Error: Ugyldig input 2"

    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
