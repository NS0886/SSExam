import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((socket.gethostname(), 8000))
socket.listen() #create a queue of 5 

    while True:
        clientsocket, address = socket.accept()
        inputfunction = raw_input("Enter add(), delete(), search(), autocomplete(), or display(): ");
        clientsocket.send(inputfunction.encode()); #send code to server to input in trie
        fromserver = clientsocket.recv(1024)
        print(fromserver.decode());  #print output of trie based on user input
        clientsocket.close() #close connection

