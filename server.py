import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((socket.gethostname(), 8000))
socket.listen(5) #create a queue of 5 
connectionlist = [socket] 

for connection in connectionlist: #this ensures integrity of order of client connection      
    while True:
        clientsocket, address = socket.accept()
        fromclient = clientsocket.recv(1024) #receive code from client
        clientsocket.send(bytes(resultfromtrie,"utf-8")) #print output of trie based on user input
        clientsocket.close() #close connection
connectionlist = [] #reset the client list
