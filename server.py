import socket               # Import socket module
import select
from threading import Thread
from queue import Queue

class Server:
	def __init__(self):
		self.s = socket.socket()         # Create a socket object
		host = 'localhost' #socket.gethostname() # Get local machine name
		port = 1337                # Reserve a port for your service.
		
		print 'Server started at ' + host
		print 'Waiting for clients...'
		
		self.s.bind((host, port))        # Bind to the port
		self.s.listen(5)                 # Now wait for client connection.
		self.connections = []

	def accept_connections(self, player_queue):
		for i in range(len(player_queue)):
			c, addr = self.s.accept()     # Establish connection with client.
			c.setblocking(0)
			print 'Got connection from', addr
			q = player_queue[i]
			t = Thread(target=self.on_new_client, args=(q,index,c,addr))	
			t.start()
			self.connections.append(t)	

	def __del__(self):
		for conn in self.connections:
			conn.join()
		self.s.close()		
	
	
	def on_new_client(self, q, client_index, clientsocket, addr):
		while True:
			ready = select.select([clientsocket], [], [], 1)
			if ready[0]:
				data = mysocket.recv(4096)
				print addr, ' >> ', data
			if not q.empty():
				msg = q.get()
				print("msg")
				if msg == "kill":
					break
				clientsocket.send(msg)
		clientsocket.close()	

