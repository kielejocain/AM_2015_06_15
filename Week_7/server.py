#!/usr/bin/python           # This is server.py file

import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection.
while True:
    c, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)

    print(s.recv(1024))
    c.send(b'Thank you for connecting')
    c.close()  # Close the connection

    # FROM http://www.tutorialspoint.com/python/python_networking.htm
