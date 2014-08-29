
def menu(Setup, Jugador):
    #Se importa el directorio de imagenes de la pantalla de login
    from misc_directory import Image_login as Image
    
    if Setup.idioma == 0:
        from lenguajes.esp import diccionario
    elif Setup.idioma == 1:
        from lenguajes.eng import diccionario
    else:
        from lenguajes.esp import diccionario
    
    #Se Cambia el nombre de las funciones por simplicidad
    Graficos = Setup.Graficos
    Cliente = Setup.Cliente
    Control = Setup.Controles
    Fichero = Setup.Ficheros
    
    #Se inicializan las variables requeridas
    largo_pantalla, ancho_pantalla = Graficos.RESOLUCION 
    font_size_titles = 30
    font_size_input = 20
    username = ""
    password = ""
    modificar_user = True
    modificar_pass = False
    boton1 = diccionario["Acceder"]
    boton2 = diccionario["Registrarse"]
    label1 = diccionario["Usuario"]
    label2 = diccionario["Contrasena"]
    try:
        username = Fichero.buscar_valor("configuracion.txt", "USERNAME")
        password = Fichero.buscar_valor("configuracion.txt", "PASSWORD")
    except:
        pass
    
    #Se cargan los recursos graficos
    Background = Graficos.cargar_imagen(Image[1], False)
    
    #Se crea un diccionario con los tamanos de cada elemento a pintar
    Sizes = {"Fondo" : (largo_pantalla, ancho_pantalla),
             "BoxUser" : (largo_pantalla * 250 / 1366, ancho_pantalla * 30 / 768),
             "BoxPass" : (largo_pantalla * 250 / 1366, ancho_pantalla * 30 / 768),
             "Botones": (largo_pantalla * 170 / 1366, ancho_pantalla * 30 / 768),
             }
    
    #Se crea una lista con los puntos donde cada elemento se imprimira
    Points = {"Fondo" : (0, 0),
              "BoxUser" : (largo_pantalla * 215 / 1366, ancho_pantalla * 605 / 768),
              "BoxPass" : (largo_pantalla * 215 / 1366, ancho_pantalla * 645 / 768),
              "InputUser" : (largo_pantalla * 220 / 1366, ancho_pantalla * 610 / 768),
              "InputPass" : (largo_pantalla * 220 / 1366, ancho_pantalla * 650 / 768),
              "LabelUser" : (largo_pantalla * 20 / 1366, ancho_pantalla * 610 / 768), 
              "LabelPass" : (largo_pantalla * 20 / 1366, ancho_pantalla * 650 / 768), 
              "BotonLogin": (largo_pantalla * 40 / 1366, ancho_pantalla * 690 / 768), 
              "BotonRegister": (largo_pantalla * 230 / 1366, ancho_pantalla * 690 / 768),
              }
    
    #Se modifican al tamaño justo de la pantalla
    Background = Graficos.resize_imagen(Background, Sizes["Fondo"])
    
    #Se establecen las fonts
    font_input = Graficos.Iniciar_texto(font_size_input)
    font_title = Graficos.Iniciar_texto(font_size_titles)
    
    #Valores de rectangulos
    box_user = (Points["BoxUser"][0], Points["BoxUser"][1], Sizes["BoxUser"][0], Sizes["BoxUser"][1])
    box_pass = (Points["BoxPass"][0], Points["BoxPass"][1], Sizes["BoxPass"][0], Sizes["BoxPass"][1])
    box_login = (Points["BotonLogin"][0], Points["BotonLogin"][1], Sizes["Botones"][0], Sizes["Botones"][1])
    box_register = (Points["BotonRegister"][0], Points["BotonRegister"][1], Sizes["Botones"][0], Sizes["Botones"][1])
    
    while True:
        #Datos para graficos
        input1 = usuario(username, 15)
        input2 = asteriscos(password, 15)
        
        #Graficos
        #Fondo
        Graficos.imprimir_imagen(Background, Points["Fondo"])
        #Labels
        Graficos.imprimir_texto(label1, (255,255,255), Points["LabelUser"], font_title)
        Graficos.imprimir_texto(label2, (255,255,255), Points["LabelPass"], font_title)
        #Cuadros de texto
        Graficos.imprimir_rectangulo((255,255,255), box_user)
        Graficos.imprimir_rectangulo((255,255,255), box_pass)
        #Input del usuario
        Graficos.imprimir_texto(input1, (0,0,0), Points["InputUser"], font_input)
        Graficos.imprimir_texto(input2, (0,0,0), Points["InputPass"], font_input)
        #Boton de login
        Graficos.imprimir_rectangulo((255,255,255), box_login)
        Graficos.imprimir_texto(boton1, (0,0,0), Points["BotonLogin"], font_title)
        #Boton de registrarse
        Graficos.imprimir_rectangulo((255,255,255), box_register)
        Graficos.imprimir_texto(boton2, (0,0,0), Points["BotonRegister"], font_title)
        
        #Prueba de frames
        Graficos.imprimir_texto(int(Graficos.obtener_frames()), (255,255,255), (0,0), font_title)
        #Quitar en produccion
        
        Graficos.actualizar_pantalla()
        Graficos.controlar_frames()