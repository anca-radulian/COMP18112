#!/usr/bin/python

import im
import time
import Tkinter
from Tkinter import *
import tkMessageBox

# Create the window

top = Tkinter.Tk()

# Add a text box to the gui
text = Text(top)
text.pack(side=TOP)

server = \
    im.IMServerProxy('http://webdev.cs.manchester.ac.uk/~mbaxaar2/IMServer.php'
                     )

# Check if there are any keys on the server
areKeys = server.keys()

# Add entry field
e1 = Entry(top, bd=5)
e1.config(state=DISABLED)
e1.pack(side=LEFT)

# Send a message state
def sendMess():
    text.config(state=NORMAL)
    text.insert(INSERT, 'Please type a message:\n')
    e1.config(state=NORMAL)
    b1.config(state=NORMAL)

# Wait for a message state
def waitingMess():
    text.config(state=NORMAL)
    text.insert(INSERT, 'Wait for the the other user message\n')
    e1.config(state=DISABLED)
    b1.config(state=DISABLED)
    top.update()
    time.sleep(1)
    while server['messageSent'] == 'false':
        if server['crash'] == 'true':
            text.insert(INSERT,
                        'The other user has crashed and has connected again\n')
            break

        time.sleep(0.05)
    server['messageSent'] = 'false'
    if server['crash'] == 'false':
        text.insert(INSERT, server['message'] + '\n')
        server['message'] = ''
    if server['crash'] == 'true':
        server['crash'] = 'false'
    sendingMess = True
    sendMess()

# The send button function
def submit():

    if server['crash'] == 'true':
        server['crash'] = 'false'
    server['message'] = e1.get()
    server['messageSent'] = 'true'
    sendingMess = False
    e1.delete(0, END)
    waitingMess()


# Add button
b1 = Button(top, text='Send', command=submit)
b1.config(state=DISABLED)
b1.pack(side=LEFT)

# If both clients are on then one must have crushed(Reconnecting)
if server['client1'] == 'on' and server['client2'] == 'on':
    sendingMess = False
    text.config(state=NORMAL)
    text.insert(INSERT, 'Reconnecting...\n')
    server['crash'] = 'true'
    time.sleep(1)
    if server['message'] == '':
       text.insert(INSERT, 'Wait for the the other user message\n')
       top.update()
    while server['message'] == '':
        time.sleep(0.5)
    text.insert(INSERT, server['message'] + "\n")
else:

 # Initialise variables on the server
    myMessage = ''
    server['messageSent'] = 'false'
    server['message'] = ''
    server['crash'] = 'false'

    # Client 1 connecting
    if not areKeys:
        sendingMess = True
        server['client1'] = 'on'
        server['client2'] = 'off'
    else:
		# Client 2 connecting
        sendingMess = False
        server['client2'] = 'on'

    client2 = server['client2']

    # Wait for client 2 if not on
    if client2 == 'off':
        text.config(state=NORMAL)
        text.delete('1.0', END)
        text.insert(INSERT, 'Waitig for client 2\n')
        text.config(state=DISABLED)
        top.update()
    while client2 != 'on':
        time.sleep(0.5)
        client2 = server['client2']



# The client sending a message and waiting for one

if sendingMess:
    text.config(state=NORMAL)
    text.insert(INSERT, 'Please type a message:\n')
    e1.config(state=NORMAL)
    b1.config(state=NORMAL)
else:
    waitingMess()


top.mainloop()
server.clear()

			
