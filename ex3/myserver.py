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
			socket.screenName = parameter
			#Save the screen name and the socket as a pair
			pair = (socket.screenName, socket)
			self.users.append(pair)
			socket.send("You have registered as " + socket.screenName)

		#print self.users

		# Sending a message to everyone( MESSAGE command)
		elif command == 'MESSAGE':
			for user in self.users:
				user[1].send(socket.screenName + ": " + parameter)

		else:
			for user in self.users:
				if command == user[0]:
					user[1].send("Private message from " + socket.screenName + ": " + parameter)
		# Signify all is well
		return True

	def onDisconnect(self, socket):
		self.noOfClients = self.noOfClients - 1
		print "A user has disconnected."
		print "Number of clients on server: " + str(self.noOfClients)



# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = MyServer()

# Start server
server.start(ip, port)
