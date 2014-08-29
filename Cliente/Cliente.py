#va a mandar mensajes

import socket
from cPickle import loads, dumps
class Cliente():
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
    
    def responder_tps(self, mensaje):
        conexion = (self.HOST, self.PORT)
        socket_cliente = socket.socket()
        socket_cliente.connect(conexion)
        while mensaje != "salir":
            try:
                mensaje = dumps(mensaje,2)
                socket_cliente.send(mensaje)
                datos_recibidos = socket_cliente.recv(4000)
                datos_recibidos = loads(datos_recibidos)
                return datos_recibidos
            except:
                return ""
        socket_cliente.close()