#!/usr/bin/python


import im
import time

server = \
    im.IMServerProxy('http://webdev.cs.manchester.ac.uk/~mbaxaar2/IMServer.php')

# Check if there are any keys on the server                  
areKeys = server.keys()

# If both clients are on then one must have crushed
if server['client1'] == 'on' and server['client2'] == 'on':
    sendingMess = False
    print "Reconnecting..."
    server['crash'] = 'true'
    time.sleep(1)
    if server['message'] == '':
    	print 'Wait for the the other user message'
    	#sendingMess = True
    while server['message'] == '':
    	time.sleep(0.5)
    print server['message']
   
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
        print 'Waitig for client 2'

    while client2 != 'on':
        time.sleep(0.5)
        client2 = server['client2']

printing = True

while True:
    # The client sending a message
    if sendingMess:
        myMessage = raw_input('Please type a message: ')
        if server['crash'] == 'true':
        	server['crash'] = 'false'
        	printing = False
        server['message'] = myMessage
        server['messageSent'] = 'true'
        sendingMess = False
        if server['message'] == 'Exit':
            break
    else:
	# The client waiting for a message
        print 'Wait for the the other user message'
        time.sleep(1)
        while server['messageSent'] == 'false':
           if server['crash'] == 'true':
                print "The other user has crashed and has connected again"
                break
        	
           time.sleep(0.05)
        server['messageSent'] = 'false'
        if server['crash'] == 'false' and printing == True:
        	print server['message']
        	if server['message'] == 'Exit':
        		server.clear()
           		break
		server['message'] = ''
        if server['crash'] == 'true':
            server['crash'] = 'false'
        sendingMess = True
        if not printing:
        	printing = True
        	print "The other user has crashed and has connected again"
        	
        

			
