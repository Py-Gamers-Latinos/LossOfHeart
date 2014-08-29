from Sqlite import Database

def crear_tabla_noticias(db):
    nombre_tabla = "Noticias"
    lista_columnas = ["ID", "Titulo", "Noticia", "Fecha", "Autor"]
    lista_valor = ["INT PRIMARY KEY", "CHAR(64)", "TEXT", "CHAR(32)", "CHAR(32)"]
    lista_NULL = [1, 1, 1, 0, 0]
    db.crear_tabla(nombre_tabla, lista_columnas, lista_valor, lista_NULL)
    
def agregar_noticia(Id, Titulo, Noticia, Fecha, Autor, db):
    nombre_tabla = "Noticias"
    lista_columnas = ["ID", "Titulo", "Noticia", "Fecha", "Autor"]
    lista_valor = [Id, Titulo, Noticia, Fecha, Autor]
    db.insertar_datos(nombre_tabla, lista_columnas, lista_valor)
    
def crear_tabla_jugadores(db):
    nombre_tabla = "Jugadores"
    lista_columnas = ["ID",
                      "Username",
                      "Password",
                      "Nombre",
                      "Email",
                      "Nivel",
                      "Experiencia",
                      "Gold",
                      "Silver",
                      "Deck",
                      "Coleccion",
                      "Rank"]
    lista_valor = ["CHAR(128) ",
                   "CHAR(32) PRIMARY KEY", 
                   "CHAR(32)", 
                   "CHAR(32)", 
                   "CHAR(32)",
                   "INT", 
                   "INT",
                   "INT",
                   "INT",
                   "TEXT",
                   "TEXT",
                   "INT"]
    lista_NULL = [1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  0,
                  0,
                  1]
    db.crear_tabla(nombre_tabla, lista_columnas, lista_valor, lista_NULL)
    
def agregar_jugador(Nombre, Username, Email, Password, db):
    def cifrado(user):
        id = ""
        for element in user:
            codigo = ord(element)
            id += str(codigo)
        return id
    nombre_tabla = "Jugadores"
    ID = cifrado(Username)
    lista_columnas = ["ID",
                      "Username",
                      "Password",
                      "Nombre",
                      "Email",
                      "Nivel",
                      "Experiencia",
                      "Gold",
                      "Silver",
                      "Rank"]
    lista_valor = [ID,
                   Username, 
                   Password, 
                   Nombre,
                   Email,
                   1, 
                   0,
                   100,
                   500,
                   0]
    db.insertar_datos(nombre_tabla, lista_columnas, lista_valor)
    
if __name__ == "__main__":
    print "Esto ha iniciado"
    db = Database("LossOfHearth")
    crear_tabla_noticias(db)
    Id = "1"
    Titulo = "'Arranque del desarrollo de Loss Of Heart'"
    Noticia = "'Es un gusto informar que a la fecha el avance en el proyecto del MMOTCG es un exito, ya contamos con la colaboracion de varios amigos interesados en el desarrollo del mismo y dia a dia avanzamos enormemente en la produccion del mismo'"
    Fecha = "'28/08/2014'"
    Autor = "'Erichris'"
    agregar_noticia(Id, Titulo, Noticia, Fecha, Autor, db)
    crear_tabla_jugadores(db)
    agregar_jugador("'Eric Christian Bernstorff Corona'", "'erichris'", "'Erichris@live.com.mx'", "'annieteamo1'", db)
    agregar_jugador("'Andrea Sanchez Martinez'", "'annieZa'", "'AnnieZa@live.com.mx'", "'tkieromuxho1'", db)
    print "Exito"
    