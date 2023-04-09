import socket
import threading
import rsa
import colorama
import random

#public_key, private_key = rsa.newkeys(1024)
#public_patner = None



# Initialize colorama
colorama.init()

# Define colors
COLORS = [colorama.Fore.BLUE, colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.MAGENTA, colorama.Fore.RED, colorama.Fore.YELLOW]

# Print ASCII art with a random color
print(f'{random.choice(COLORS)}''''
  _    _         
 | |  | |___________ _   _  ____ __   _ _     ______    _   _
 | |__| |   | | ____| |_/ /|_   |||  //| |___    || |  | |_/ /
 |  __  |___| | |   |    / || __|||_// |  ___|___|| |  |    /
 | |  | | @ @ | |___|  _   | |__ | |/  | |___ @ @|| |__|  _ \\
 |_|  |_|_@_@_|_____|_| |_ |____||_|   |_____|____|____|_| |_\\'''+
      colorama.Style.RESET_ALL)

# Reset colorama
colorama.deinit()

nickname = input("choose a nickname: ....")



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.103",9999))
#public_patner = rsa.PublicKey.load_pkcs1(client.recv(1024))
#client.send(public_key.save_pkcs1("PEM"))
#public_patner = rsa.PublicKey.load_pkcs1(client.recv(1024), format='PEM')



def recieve():
    while True:
        try:
           # message = rsa.decrypt(client.recv(1024), private_key).decode()
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        #client.send(rsa.encrypt(message.encode(), public_patner))
        client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
