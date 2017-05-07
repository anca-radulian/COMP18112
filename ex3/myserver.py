import sys
from ex3utils import Server

# Create an echo server class
class MyServer(Server):

	def onStart(self):
		print "My server has started"
		self.noOfClients = 0
		self.users = []



	def onConnect(self, socket):
		self.noOfClients = self.noOfClients + 1
		# Initialise connection specific variables
		socket.screenName = None
		print "A client has connected."
		print "Number of clients on server: " + str(self.noOfClients)


	def onMessage(self, socket, message):
		print "New message received."
		(command, sep, parameter) = message.strip().partition(' ')

		# Act upon REGISTER message

		if command == 'REGISTER':
			used = False
			for user in self.users:
				if parameter == user[0]:
					used = True
					socket.send("Please choose another name using "
					 			+ "command REGISTER")
				

			if used == False and socket.screenName != None:
				for user in self.users:
					if user[0] == socket.screenName:
						self.users.remove(user)
				socket.screenName = parameter
				pair = (socket.screenName, socket)
				self.users.append(pair)
				socket.send("You have registered as " + socket.screenName)
			if used == False and socket.screenName == None:
				socket.screenName = parameter
				#Save the screen name and the socket as a pair
				pair = (socket.screenName, socket)
				self.users.append(pair)
				socket.send("You have registered as " + socket.screenName)


		# Sending a message to everyone( MESSAGE command)
		elif command == 'MESSAGE' and socket.screenName != None:
			if parameter == 'logout':
				return False
			else:
				for user in self.users:
					user[1].send(socket.screenName + ": " + parameter)

		else:
			for user in self.users:
				if command == user[0] and socket.screenName != None:
					user[1].send("Private message from " + socket.screenName
								  + ": " + parameter)
		# Signify all is well
		return True

	# Delete the user from the list after disconnecting
	def onDisconnect(self, socket):
		self.noOfClients = self.noOfClients - 1
		for user in self.users:
			if user[0] == socket.screenName:
				self.users.remove(user)

		print "A user has disconnected."
		print "Number of clients on server: " + str(self.noOfClients)



# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = MyServer()

# Start server
server.start(ip, port)
