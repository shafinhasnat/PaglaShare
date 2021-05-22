import tkinter
from tkinter import filedialog, Label
import os
import threading
import socket
from app import Server
root = tkinter.Tk()
root.resizable(False, False)
root.geometry('350x120')
open(".file", "w+").close()
file = open('.file', 'r')
if len(file.read()) == 0:
	text = "No file selected :("
else:
	text = file.read()
label = Label(root, wraplength=300, justify="center", text=text)
	
def serverLabel():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = 'Server running at http://{}:1609'.format(s.getsockname()[0])
	s.close()
	ip = Label(root, fg='green', text=ip)
	ip.pack()

def uploadFile():
	path =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
	if len(path) == 0:
		text = "No file selected :("
	else:
		text = path
	label.config(text=text)
	file = open(".file", "w")
	file.write(path)
def server():
	server = Server()
	server.app.run(host="0.0.0.0", port="1609")
def startServer():
	th = threading.Thread(target=server, args=[])
	th.daemon = True
	th.start()


if __name__ == '__main__':
	serverLabel()
	share = tkinter.Button(root, text="share", command=uploadFile).pack()
	startServer()
	label.pack()
	root.title("PaglaShare")
	root.mainloop()
