#Serivodr para manejar diferentes eventos
import SocketServer
import threading
#import time
from cPickle import dumps, loads
from event_handler.eventHandler import EventHandler
from setup import Setup

class MiTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		package = ""
		config = Setup()
		while package != "salir":
			try:
				package = self.request.recv(4000)
				package = loads(package)
				print package
				mensaje = EventHandler(package, config)
				mensaje = dumps(mensaje)
				self.request.sendall(mensaje)
			except:
				pass
			
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
	pass
	
def servidor(host, port):
	conexion = (host,port)
	server =  ThreadServer(conexion, MiTCPHandler)
	server_thread = threading.Thread(target = server.serve_forever)
	server_thread.start()
	

