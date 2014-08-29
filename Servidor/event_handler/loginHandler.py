


def LoginHandler(package, config):
    if package["Action"] == 1:
        # 1.- login 2.- wrong pass 3.- wrong username
        user = package["Username"]
        password = package["Password"]
        try:
            condicion = "username = '%s'" % user
            real_pass = config.Database.obtener_registro("Jugadores", ["password"], condicion)
            real_pass = real_pass[0][0]
            if real_pass == password:
                datos = ["ID", "username", "nivel", "experiencia", "gold", "silver", "deck", "coleccion", "rank"]
                jugador = config.Database.obtener_registro("Jugadores", datos, condicion)[0]
                temp = {}
                for time in range(0, len(datos)):
                    temp[datos[time]] = jugador[time]
                jugador = temp
                return {"Status": True, "Answer": jugador}
            else:
                return {"Status": False, "Answer": 2}
        except:
            return {"Status": False, "Answer": 3}