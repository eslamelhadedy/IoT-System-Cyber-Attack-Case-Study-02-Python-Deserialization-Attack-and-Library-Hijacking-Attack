import zmq
import pickle
iotIP = '172.23.155.209'
port = 3003

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:%s" %(iotIP,port))
print("Sending request btyes via ZMQ client:")
configData = {
    'TEST_MD': None , 
    'RADAR_TYPE':None,
    'RADAR_PORT': None,
    'RADAR_UPDATE_INTERVAL': None,
    'RPT_MD': None,
    'RPT_INT': None,
    'RPT_SER_IP': None,
    'RPT_SER_PORT': None,
    'WEB_PORT': None
}
pickledata = pickle.dumps(configData, protocol=pickle.HIGHEST_PROTOCOL)
print(str(pickledata))
socket.send(pickledata)
#  Get the reply.
replyData = socket.recv()
print("received reply bytes:")
print(str(replyData))
reqDict = pickle.loads(replyData)
print ("Received reply: \n %s" %str(reqDict))