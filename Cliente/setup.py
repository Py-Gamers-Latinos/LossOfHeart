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

from Cliente import Cliente
from Control import Control
from Graficos import Graficos
from Fichero import Fichero


class Setup():
    def __init__(self):
        #Inicializamos la clase fichero para acceder a las variables de configuracion
        self.iniciar_ficheros()
        self.iniciar_conexion()
        self.verificar_estado_servidor()
        self.iniciar_graficos()
        self.iniciar_controles()
        self.cargar_idioma()
        
    def iniciar_ficheros(self):
        self.Ficheros = Fichero()
        
    def iniciar_conexion(self):
        #Se cargan los valores necesarios del archivo configuracion.txt
        host = self.Ficheros.buscar_valor("configuracion.txt", "HOST_SERVER")
        port = self.Ficheros.buscar_valor("configuracion.txt", "PORT_SERVER")
        self.Cliente = Cliente(host, int(port))
    
    def verificar_estado_servidor(self):
        pass
    
    def iniciar_graficos(self):
        self.Graficos = Graficos()
        
        #Se cargan las frames
        FPS = int(self.Ficheros.buscar_valor("configuracion.txt", "FPS"))
        self.Graficos.establecer_frames(FPS)
        
        #Se cargan los valores de la resolucion del archivo Configuracion.txt
        largo_pantalla = int(self.Ficheros.buscar_valor("configuracion.txt", "LARGO_PANTALLA"))
        ancho_pantalla = int(self.Ficheros.buscar_valor("configuracion.txt", "ANCHO_PANTALLA"))
        fullscreen = int(self.Ficheros.buscar_valor("configuracion.txt", "FULLSCREEN"))
        nombre_app = self.Ficheros.buscar_valor("configuracion.txt", "NOMBRE_APP")
        version_app = self.Ficheros.buscar_valor("configuracion.txt", "VERSION_APP")
        self.Graficos.RESOLUCION = (largo_pantalla, ancho_pantalla)
        
        #Se establece la pantalla y se cargan titulos y demas
        self.Graficos.establecer_pantalla(self.Graficos.RESOLUCION, fullscreen)
        self.Graficos.titulo_ventanta(nombre_app + " " + version_app)
        
        #Pendiente cargar icono
        
    def iniciar_controles(self):
        self.Controles = Control()
        self.Controles.repeat(400, 50)
        
    def cargar_idioma(self):
        #self.idioma = 0 para español y self.idioma = 1 para ingles
        self.idioma = int(self.Ficheros.buscar_valor("configuracion.txt", "IDIOMA"))
    
    
    
    




##Conexion a servidor


#Comprobar estado del servidor





