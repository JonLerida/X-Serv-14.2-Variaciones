#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
# tenemos que convertir el string en bytes
# la función bytes (string, 'codificacion') lo hace
# HTML-->
# <h1> es como head o título
#<p> es parrafo 
#<img src = 'url' width = ''> etc
mySocket.listen(5)
#Devuelve un 200 OK y una imagen
while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", 'utf-8') +
                    bytes("<html><body><h1>Asos</h1></body></html>", 'utf-8') +
                    bytes("<meta http-equiv='refresh' content='1; url=http://asos.com'>", 'utf-8')+
                    bytes("\r\n", 'utf-8'))
    recvSocket.close()
