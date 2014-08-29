
# 1 = Server Status
def CheckServerHandler(package):
    if package["Action"] == 1:
        from Fichero import Fichero
        Ficheros = Fichero()
        server_status = Ficheros.buscar_valor("configuracion.txt", "SERVER_STATUS")
        del Ficheros
        if int(server_status) == 1:
            return {"Status": True, "Answer": "Server is Online"}
        elif int(server_status) == 0:
            return {"Status": False, "Answer": "El servidor esta Offline"}
        elif int(server_status) == 2:
            return {"Status": False, "Answer": "El Servidor esta en mantenimiento"}
        
    
    #Falta implementar la funcion de cuando el servidor esta en mantenimiento
    