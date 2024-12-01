# send text from input via socket 
from socket import *
serverName = '192.168.1.10'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Input sentence to send:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()


# send file with socket 
serverName = '192.168.1.10'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
file_name = input("enter complete file name")
s = socket(AF_INET,SOCK_DGRAM)

buf =1024
addr = (serverName,serverPort)
s.sendto(file_name,addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print( "sending ...")
        data = f.read(buf)
s.close()
f.close()