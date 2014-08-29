#!/usr/bin/env python
# -*- coding: utf-8 -*-
                    ##################################################
                    #Proyecto:                                       #
                    #Version: 0.0.1                                  #
                    #Nombre:Py. Gamers Latinos                       #
                    #Fecha de inicio: 24/08/2014                     #
                    #Fase: En desarrollo                             #
                    ##################################################
                    
#Datos y configuracion basica del juego.

from setup import Setup
from loginApplication.loginScreen import login
from ClientHandler import check_server

if __name__ == '__main__':
    #Se carga la configuracion del juego
    Setup = Setup()
    
    #Verificar disponibilidad del servidor de juegos
    respuesta = check_server(Setup.Cliente)
    
    if respuesta[0] == True:
        pass
    else:
        print respuesta[1]
        exit()
    #1 .- Pantalla de login
    #2 .- Pantalla de menu
    status = 1
    while True:
        #Pantalla de logeo
        if status == 1:
            Jugador = login(Setup)
            status = 2
        elif status == 2:
            
            
    
    
    