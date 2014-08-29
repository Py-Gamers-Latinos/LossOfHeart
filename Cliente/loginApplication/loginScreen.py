#!/usr/bin/env python
# -*- coding: utf-8 -*-
                    ##################################################
                    #Proyecto:                                       #
                    #Version: 0.0.1                                  #
                    #Nombre:Py. Gamers Latinos                       #
                    #Fecha de inicio: 24/08/2014                     #
                    #Fase: En desarrollo                             #
                    ##################################################

def login(Setup):
    from ClientHandler import logeo
    
    def asteriscos(text, limit):
        new_text = ""
        if len(text) >= limit:
            new_text = "*"*limit
            return new_text
        for letter in text:
            new_text += "*"
        return new_text
    def usuario(text, limit):
        new_text = ""
        if text != "":
            if limit >= len(text):
                new_text = text[-len(text):-1] + text[-1]
            else:
                new_text = text[-limit:-1] + text[-1]
            return new_text
        else:
            return new_text
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
        
                              
        #Controles
        accion = Control.eventos_poll()
        if accion == "click derecho":
            if Control.dentro_de(Points["BoxUser"], Sizes["BoxUser"]):
                #Si se selecciona el cuadro de usuario
                modificar_user = True
                modificar_pass = False
            elif Control.dentro_de(Points["BoxPass"], Sizes["BoxPass"]):
                #Si se selecciona el cuadro de password
                modificar_user = False
                modificar_pass = True
            elif Control.dentro_de(Points["BotonLogin"], Sizes["Botones"]):
                #Si se presiona el boton de login
                try:
                    mensaje = logeo(Cliente, username, password)
                    if mensaje[0] == True:
                        return mensaje[1]
                    elif mensaje[0] == False and mensaje[1] == 2:
                        print "Wrong password"
                    elif mensaje[0] == False and mensaje[1] == 3:
                        print "Wrong username and password"
                except:
                    print "No hubo respuesta del servidor"
            #===================================================================
            # elif Control.dentro_de(Boton2["Position"], Boton2["Size"]):
            #     #Si se presiona el boton de login
            #     register_app.register(Graficos, Control, Cliente, Misc_path)
            #===================================================================
            else:
                #Si se presiona en otro punto
                modificar_user = False
                modificar_pass = False
        elif accion in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 @.,-_":
            if modificar_user == True:
                username += accion
            if modificar_pass == True:
                password += accion
        elif accion == "backspace":
            if modificar_user == True:
                username = username[0:len(username)-1]
            elif modificar_pass == True:
                password = password[0:len(password)-1]
        elif accion == "tab":
            if modificar_user == True:
                modificar_user = False
                modificar_pass = True
            elif modificar_user == False:
                modificar_user = True
                modificar_pass = False
        #Conexion con servidor