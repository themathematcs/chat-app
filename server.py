import socket
import threading
import rsa

#public_key, private_key = rsa.newkeys(1024)
#public_patner = None
#client.send(public_key.save_pkcs1("PEM"))
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.103', port))
server.listen()




clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        #client.send(rsa.decrypt(message.encode('ascii'), public_patner))
        client.send(message)

def handle(client):
    while True:
        try:
          

            message = client.recv(1024)
            broadcast(message)

        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        #client.send(public_key.save_pkcs1("PEM"))
        #public_patner = rsa.PublicKey.load_pkcs1(client.recv(1024))

        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        #nickname = rsa.decrypt(client.recv(1024), private_key).decode()
        #nickname = rsa.decrypt(client.recv(1024), private_key).decode()
        print(nickname)
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f' {nickname} joined the chat!'.encode('ascii'))
        print('>>>>                                       <<<<<')

        client.send("connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is listening .....")
receive()
