import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)
public_patner = None

host_ip = socket.gethostbyname(socket.gethostname())


choice = input("do you want to host(1) or do you want to serve(2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, 9999))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_patner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host_ip , 9999))
    public_patner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
   
else:
    exit()


def sending_messages(c):
    while True:
        messages = input("")
        c.send(rsa.encrypt(messages.encode(), public_patner))
        print("you: " + messages)

def receiving_messages(c):
    while True:
       
        print("patner: " + rsa.decrypt(c.recv(1024), private_key).decode())


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()

