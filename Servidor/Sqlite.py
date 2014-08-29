'''
Created on 27/08/2014

@author: HP
'''
import sqlite3
import os



class Database():
    def __init__(self, ruta_relativa):
        #ruta_relativa = "carpeta/database"
        PATH = os.path.dirname(os.path.realpath(__file__))
        self.connection = sqlite3.connect(PATH + "/" + ruta_relativa)
        self.cursor = self.connection.cursor()
        
    def crear_tabla(self, nombre_tabla, lista_columnas, lista_valor, lista_NULL):
        #nombre_tabla = "Nombre de la tabla"
        #lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
        #lista_valor = ["INT PRIMARY KEY", "TEXT", "INT", "CHAR(50)", "REAL"]
        #lista_NULL = [1, 1, 1, 0, 0]
        comando = "DROP TABLE IF EXISTS " + nombre_tabla
        self.cursor.execute (comando)
        command = "CREATE TABLE %s" % nombre_tabla
        table = "("
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time] + " "
            table += lista_valor[time] + " "
            if time == len(lista_columnas) - 1:
                pass
            elif lista_NULL[time] == 1:
                table += "NOT NULL, "
            else:
                table += ", "
        table += ")"
        command += table
        self.cursor.execute(command)
        self.connection.commit()
        
    def insertar_datos(self, nombre_tabla, lista_columnas, lista_valor):
        #nombre_tabla = "Nombre de la tabla"
        #lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
        #lista_valor = ["INT PRIMARY KEY", "TEXT", "INT", "CHAR(50)", "REAL"]
        command = "INSERT INTO "
        table = nombre_tabla
        table += "("
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += ") VALUES ("
        for time in range(0, len(lista_valor)):
            table += str(lista_valor[time])
            if time != len(lista_valor) - 1:
                table += ", "
            else:
                table += ")"
        command += table
        self.cursor.execute(command)
        self.connection.commit()
        
    def obtener_registros(self, nombre_tabla, lista_columnas):
        command = "SELECT "
        table = ""
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += " from "
        table += nombre_tabla
        command += table
        self.cursor.execute(command)
        registros = []
        time = 0
        for registro in self.cursor:
            registros.append([])
            for element in registro:
                registros[time].append(element)
            time += 1
        return registros
    
    def actualizar_registro(self, nombre_tabla, colum_value, ID_value):
        #nombre_tabla = "Nombre de tabla"
        #colum_value = "nombre = 'Christian'"
        #ID_value = "ID = 001"
        command = "UPDATE "
        table = nombre_tabla + " set "
        table += colum_value
        table += " where "
        table += ID_value
        command += table
        self.cursor.execute(command)
        self.connection.commit()
        
    def eliminar_registro(self, nombre_tabla, ID_value):
        command = "DELETE from "
        table = nombre_tabla
        table += " where "
        table += ID_value
        command += table
        self.cursor.execute(command)
        self.connection.commit()
        
    def obtener_registro(self, nombre_tabla, lista_columnas, ID_value):
        command = "SELECT "
        table = ""
        for time in range(0, len(lista_columnas)):
            table += lista_columnas[time]
            if time != len(lista_columnas) - 1:
                table += ", "
            else:
                table += " from "
        table += nombre_tabla
        table += " where "
        table += ID_value
        command += table
        self.cursor.execute(command)
        registros = []
        time = 0
        for registro in self.cursor:
            registros.append([])
            for element in registro:
                registros[time].append(element)
            time += 1
        return registros
        
#===============================================================================
# if __name__ == "__main__":
#     db = Database("prueba")
#===============================================================================

    #===========================================================================
    # lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
    # lista_valor = ["INT PRIMARY KEY", "TEXT", "INT", "CHAR(50)", "REAL"]
    # lista_NULL = [1, 1, 1, 0, 0]
    # db.crear_tabla("Tabla_de_prueba", lista_columnas, lista_valor, lista_NULL)
    #===========================================================================
    
    #===========================================================================
    # lista_columnas = ["Id", "Nombre", "Edad", "Direccion", "Salario"]
    # lista_valor = ["'001'", "'chris'", "22", "'Paseo de me la pela'", "12000.01"]
    # db.insertar_datos("Tabla_de_prueba", lista_columnas, lista_valor)
    #===========================================================================
    
    #===========================================================================
    # db.actualizar_registro("Tabla_de_prueba", "nombre = 'Christian'", "nombre = 'eric'")
    #===========================================================================
    
    #===========================================================================
    # db.eliminar_registro("Tabla_de_prueba", "ID = 1")
    #===========================================================================
    
    #===========================================================================
    # lista_columnas = ["id", "nombre", "Edad"]
    # registro = db.obtener_registro("Tabla_de_prueba", lista_columnas, "ID = 002")
    # print registro
    #===========================================================================
    
    #===========================================================================
    # lista_columnas = ["id", "nombre", "Edad"]
    # registro = db.obtener_registros("Tabla_de_prueba", lista_columnas)
    # print registro
    #===========================================================================