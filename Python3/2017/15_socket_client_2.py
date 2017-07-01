#!/usr/bin/env python3

import socket
 
def Main():
    host = '127.0.0.1'
    port = 9999
     
    mySocket = socket.socket()
    mySocket.connect((host,port))
     
    message = input(" -> ")
     
    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
         
        print ('Received from server: ' + data)
         
        message = input(" -> ")
	     
    mySocket.close()
 
if __name__ == '__main__':
    Main()
