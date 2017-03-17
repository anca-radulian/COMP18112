import im
import time
server = im.IMServerProxy('http://webdev.cs.manchester.ac.uk/~mbaxaar2/IMServer.php')
areKeys =  server.keys()

if not areKeys:
    sendingMess = True
    waitingMess = False
    server['client1'] = 'on'
    server['client2'] = 'off'
else:
    sendingMess = False
    waitingMess = True
    server['client2'] = 'on'

client2 = server['client2']

if client2 == 'off':
    print "Waitig for client 2"

while client2 != 'on':
    time.sleep(2)
    client2 = server['client2']

myMessage = ""
while True:

    if sendingMess:
        myMessage = raw_input("Please type a message: ")
        server['message'] = myMessage
        sendingMess = False
        waitingMess = True
        if server['message'] == "Exit":
            break
    else:
        print "Wait for the the other user message"
        time.sleep(15)
        print server['message']
        if server['message'] == "Exit":
            server.clear()
            break
        del server['message']
        sendingMess = True
        waitingMess = False
