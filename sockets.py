import socket
#                       internett            TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        local host
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
