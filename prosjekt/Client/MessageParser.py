import json

""" Format
{
'timestamp': <timestampt>,
 'sender': <username>,
 'response': <response>,
 'content': <content>,
 } 
 """
class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
	    # More key:values pairs are needed	done
        }

    def parse(self, payload):
        # decode the JSON object
        payload_dumped = json.loads(payload)
        #print payload
        #print payload['response']
        if payload_dumped['response'] in self.possible_responses:
            return self.possible_responses[payload_dumped['response']](payload_dumped)
        else:
            return "[*] Error! Ugyldig repons!"
            # Response not valid

    def parse_error(self, payload):
        return_string = ""
        return_string += "Tid sendt: "+str(payload['timestamp'].split(" ")[1])+" "+str(payload['timestamp'].split(" ")[2])+" "+str(payload['timestamp'].split(" ")[3])+"\n"
        return_string += "Avsender: "+payload['sender']+"\n"
        return_string += "Respons: "+payload['response']+"\n"
        return_string += "Innhold: "+payload['content']
        return return_string
    
    def parse_info(self, payload):
        return_string = ""
        return_string += "Tid sendt: "+str(payload['timestamp'].split(" ")[1])+" "+str(payload['timestamp'].split(" ")[2])+" "+str(payload['timestamp'].split(" ")[3])+"\n"
        return_string += "Avsender: "+payload['sender']+"\n"
        return_string += "Respons: "+payload['response']+"\n"
        return_string += "Innhold: "+payload['content']
        return return_string
    def parse_message(self,payload):
        return_string = ""
        return_string += "Tid sendt: "+str(payload['timestamp'].split(" ")[1])+" "+str(payload['timestamp'].split(" ")[2])+" "+str(payload['timestamp'].split(" ")[3])+"\n"
        return_string += "Avsender: "+payload['sender']+"\n"
        return_string += "Respons: "+payload['response']+"\n"
        return_string += "Innhold: "+payload['content']
        return return_string

    def parse_history(self,payload):
        return_string = ""
        return_string += "Tid sendt: "+str(payload['timestamp'].split(" ")[1])+" "+str(payload['timestamp'].split(" ")[2])+" "+str(payload['timestamp'].split(" ")[3])+"\n"
        return_string += "Avsender: "+payload['sender']+"\n"
        return_string += "Respons: "+payload['response']+"\n"
        return_string += "Innhold: "+payload['content']
        return return_string

    
    # Include more methods for handling the different responses... 
