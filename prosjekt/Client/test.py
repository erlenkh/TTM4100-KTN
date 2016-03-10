
import re, json



test = '{"timestamp": "time","sender": "user","response": "resp", "content": "cont"}'
jsonting = json.loads(test)
#print jsonting

jsondump = json.dumps(jsonting)
#print jsondump

regex = re.compile(r'{"timestamp": "(.*)", "sender": "(.*)", "response": "(.*)", "content": "(.*)""}', re.M | re.I)

#regex = re.compile(r'\d{1,}.: (.*) (\d{1,}):')


teststring = '{"timestamp": "ost", "sender": "kake", "response": "faen", "content": "iannen" }'
regsearch = regex.search(teststring)

#print regsearch


#print jsonting['timestamp']


pattern = re.compile(r'\w{0,}')



i = "ostekake"
if re.search('[A-Za-z0-9]+', "ostekake"):
    print i

if i:
	print "t"