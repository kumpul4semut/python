#!/usr/bin/env python

#Load Module
import socket
import time
import datetime

# Inisisal server
s = socket.socket()        
host = socket.getfqdn()
port = 1212
        


if (host != "127.0.0.1"):
    host = "127.0.0.1"
s.bind((host, port))  
s.listen(5) 

# load webserver
while True:
    
    #info for time connection
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Establish connection with client.    
    c, (client_host, client_port) = s.accept()

    # Maximal connection
    c.recv(1000)

    # Load data for browser true 
    c.send(b'HTTP/1.0 200 OK\n')
    c.send(b'Content-Type: text/html\n')
    c.send(b'\n')
    c.send(b"""
        <html>
        <head>
          <style>
          h1{
            color:red;
            }
          </style>
        </head>
        <body>
        <h1>Hello World</h1> this is my server!
        </body>
        </html>
    """)
    c.close()