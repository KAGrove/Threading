import threading
import socket

host = '127.0.0.1' # localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f'{nickname} left the chat!'.encode('cp865'))
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}") #So admin knows

        client.send('NICK'.encode('cp865')) #Client informed to write nickname
        nickname = client.recv(1024).decode('cp865') #Receive nickname from client
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!') #So admin knows
        broadcast(f'{nickname} joined the chat!'.encode('cp865'))
        client.send('Connected to the server!'.encode('cp865')) #To particular client

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
