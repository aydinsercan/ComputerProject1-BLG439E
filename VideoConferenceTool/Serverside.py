
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import socket


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client): 
    name = client.recv(BUFSIZ).decode("utf8")
    print(name)
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        print(msg)
        if msg.decode()[0:7] == "getFile":
            msg=msg.decode()[7:]
            print("MSG:",msg)
            print("getFile")
            if not os.path.exists(msg):
                print("doesnt exist file")
                client.send("file-doesn't-exist".encode())

            else:
                print("file Exists")
                client.send("file-exists".encode())
                print('Sending',msg)
                if msg != '':
                    file = open(msg,'rb')
                    dosyaici = file.read(1024)
                    print("Dosya ici:", dosyaici, type(dosyaici))
                    while dosyaici:
                        client.send(dosyaici)
                        dosyaici = file.read(1024)

                    client.close()
                    
        elif msg != bytes("{quit}", "utf8"):
            print("message")
            broadcast(msg, name+": ")
        
        else: 
            client.send(bytes("{quit}", "utf8"))
            print("quitting" + msg)
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = 'localhost'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()