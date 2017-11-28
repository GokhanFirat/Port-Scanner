import socket

client = socket.socket()

host = raw_input("Host : ")

print """
	   -------------------------------------------------------------------
	   |if you want to scan only one port please enter 0 of maxPort value|
	   -------------------------------------------------------------------
	"""

port = int(raw_input("Port : "))
maxPort = int(raw_input("Max Port : "))

if maxPort == 0:
	try:
		print host + ":" + str(port) + " try to connect adress..."
		client.connect((host,port))
		client.send('Connect')
		result = client.recv(1024)
		if result:
			print result+" port " + str(port) + " open"
			client.close()
	except:
			print "Error !"
if (port > 0 and maxPort > 0):
	for portNo in range(port,maxPort):
		try:
			print host + ":" + str(portNo) + " try to connect adress..."
			client.connect((host,portNo))
			s.send('Connect')
			result = client.recv(1024)
			if result:
				print result+" port " + str(port) + " open"
				client.close()
		except:
			print "Error!"


