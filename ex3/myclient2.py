"""

IRC client exemplar.

"""

import sys
from ex3utils import Client

import time
# GUI
import Tkinter
from Tkinter import *
import tkMessageBox

# Create the window
top = Tkinter.Tk()

# Add a text box to the gui
text = Text(top)
text.pack(side=TOP)

# Add entry field
e1 = Entry(top, bd=5)
e1.pack(side=LEFT)

def toggle():
	if b2.config('relief')[-1] == 'sunken':
		b2.config(relief="raised")
	else:
		b2.config(relief="sunken")

def submit():
	if e1.get() == 'logout':
		client.stop()
		top.quit()
		top.destroy()
	elif b2.config('relief')[-1] == 'sunken':
		client.send(e1.get())
		e1.delete(0, END)
	elif e1.get().split(" ")[0] == "REGISTER":
		client.send(e1.get())
		e1.delete(0, END)
	else :
		client.send('MESSAGE ' + e1.get())
		e1.delete(0, END)


# Add buttons
b1 = Button(top, text='Send', command=submit)
b1.pack(side=LEFT)

b2 = Button(top, text='Private', command=toggle, relief="raised" )
b2.pack(side=LEFT)

class IRCClient(Client):

	def onMessage(self, socket, message):
	# *** process incoming messages here ***
		text.config(state=NORMAL)
		text.insert(INSERT, message + "\n")
		return True


# Parse the IP address and port you wish to connect to.
ip = sys.argv[1]
port = int(sys.argv[2])
screenName = sys.argv[3]

# Create an IRC client.
client = IRCClient()

# Start server
client.start(ip, port)

# *** register your client here, e.g. ***
client.send('REGISTER %s' % screenName)

top.mainloop()
client.stop()
