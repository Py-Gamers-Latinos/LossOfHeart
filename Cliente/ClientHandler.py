
def check_server(Cliente):
    package = {"Status": 1, "Action": 1}
    answer = Cliente.responder_tps(package)
    if answer["Status"] == True:
        return (True, "Online")
    else:
        return (False, answer["Answer"])
    

def logeo(Cliente, username, password):
    mensaje = {"Status": 2, "Action": 1, "Username": username, "Password": password}
    recibido = Cliente.responder_tps(mensaje)
    if recibido["Status"] == True:
        from jugador import Jugador
        player = recibido["Answer"]
        Jugador = Jugador()
        Jugador.establecer_Id(player["ID"])
        Jugador.establecer_nombre("username")
        Jugador.establecer_nivel("nivel")
        Jugador.establecer_experiencia("experiencia")
        Jugador.establecer_gold("gold")
        Jugador.establecer_silver("silver")
        Jugador.establecer_deck("deck")
        Jugador.establecer_coleccion("coleccion")
        Jugador.establecer_rank("rank")
        return (True, Jugador)
    else:
        error = recibido["Answer"]
        return (False, error)