
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import socket
import os


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


def send(event=None):
    msg = my_msg.get()
    my_msg.set("") 
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def sendFile(event=None):
    sendingFileName = "sentFile" + file_name.get()

def getFile(event=None):
    gettingfileName = "getFile" + file_name.get()
    client_socket.send(bytes(gettingfileName,"utf-8"))
    print("sended")
    confirmation = client_socket.recv(1024)
    print("confirmed",confirmation.decode())
    if confirmation.decode() == "file-doesn't-exist":
        print("File doesn't exist on server.")


    else:        
        write_name = 'from_server '+ gettingfileName
        if os.path.exists(write_name): os.remove(write_name)

        f = open(write_name,"w")
        f.write(confirmation.decode())
        f.close()

def reconnect():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(ADDR)


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

def VideoShare(event=None):
    print("")

top = tkinter.Tk()
top.title("ZomZom")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() 
my_msg.set("Type your messages here.")

file_name = tkinter.StringVar()
file_name.set("Type file path here.")

scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

entry_file = tkinter.Entry(top, textvariable=file_name)
entry_file.bind("<Return>", file_name)
entry_file.pack()
send_file_button = tkinter.Button(top, text="Send File", command=sendFile)
send_file_button.pack()

get_file_button = tkinter.Button(top, text="Get File", command=getFile)
get_file_button.pack()

get_file_button = tkinter.Button(top, text="Video Share", command=VideoShare)
get_file_button.pack()

get_file_button = tkinter.Button(top, text="Screen Share", command=VideoShare)
get_file_button.pack()


top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = "localhost"
PORT = 33000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() 