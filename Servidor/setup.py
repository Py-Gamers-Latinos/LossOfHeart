#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Created on 22/07/2014

@author: Erichris
Contact: 442-4-59-94-75
E-mail: erichris@live.com.mx
Proyect name: Time Travel
Version: 0.0.1
Description: RPG TCG based on the mitos y leyendas TCG of SALO�s company that broke some years ago.
             This game will have a PVP mode, adventurer mode and tournament mode.
             The lenguage will be spanish in alpha release.

'''
from Postresql import Database as PSQL 
from Sqlite import Database as SQL
from Fichero import Fichero

class Setup():
    def __init__(self):
        self.iniciar_ficheros()
        self.iniciar_database()
        self.conf_servidor()
    
    def iniciar_ficheros(self):
        self.Fichero = Fichero()
        
    def iniciar_database(self):
        database = int(self.Fichero.buscar_valor("configuracion.txt", "DATABASE"))
        if database == 0:
            puerto = self.Fichero.buscar_valor("configuracion.txt", "DBPORT")
            nombredb = self.Fichero.buscar_valor("configuracion.txt", "DBNAME")
            usuario = self.Fichero.buscar_valor("configuracion.txt", "DBUSER")
            password = self.Fichero.buscar_valor("configuracion.txt", "DBPASS")
            self.Database = PSQL()
            self.Database.crear_conexion(puerto, nombredb, usuario, password)
        elif database == 1:
            self.Database = SQL("LossOfHearth")
        
    def conf_servidor(self):
        host = self.Fichero.buscar_valor("configuracion.txt", "HOST_SERVER")
        port = self.Fichero.buscar_valor("configuracion.txt", "PORT_SERVER")
        self.host = host
        self.port = int(port)



