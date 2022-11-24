import socket
import sys
import time

s = socket.socket()
host = input(str('Host name: '))
port = 1478

try:
    s.connect((host, port))
    print('Connected to Server')

except:
    print('Connection to Server is failed :(')

while 1:
    incoming_messenge = s.recv(1024)
    incoming_messenge = incoming_messenge.decode()
    print('Server: ', incoming_messenge)
    message = input(str('You: '))
    message = message.encode()
    s.send(message)