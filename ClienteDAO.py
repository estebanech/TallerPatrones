import pymysql
from DbConector import DbConector
from Cliente import Cliente
import pandas as pd
import datetime
class ClienteDAO:
    def __init__(self):
        self.DB = DbConector.getInstancedb()
        self.DBconection = DbConector.getInstance()
    def getallclientes(self):
        sql = """SELECT * FROM Clientes"""
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "nombre", "apellidos", "genero", "fecha nacimiento", "estado civil"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["nombre"] = fat_panda["nombre"].astype(str)
            fat_panda["apellidos"] = fat_panda["apellidos"].astype(str)
            fat_panda["genero"] = fat_panda["genero"].astype(str)
            fat_panda["fecha nacimiento"] = fat_panda["fecha nacimiento"].astype(str)
            fat_panda["estado civil"] = fat_panda["estado civil"].astype(str)
            for row in results:
                temp = list(row)
                temp[4] = '{0:%Y-%m-%d}'.format(temp[4])
                panda = pd.DataFrame([temp], columns= ["id", "nombre", "apellidos", "genero", "fecha nacimiento", "estado civil"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            clientes = []
            for index, row in fat_panda.iterrows():
                cliente = Cliente(row["nombre"], row["apellidos"],row["genero"], row["fecha nacimiento"], row["estado civil"],row["id"])
                clientes.append(cliente)
            return clientes
        except:
            raise Exception("No se pudo extraer los clientes")
    def getclientebyid(self,id):
        sql = "SELECT * FROM Clientes WHERE Id = '%d'" % (id)
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "nombre", "apellidos", "genero", "fecha nacimiento", "estado civil"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["nombre"] = fat_panda["nombre"].astype(str)
            fat_panda["apellidos"] = fat_panda["apellidos"].astype(str)
            fat_panda["genero"] = fat_panda["genero"].astype(str)
            fat_panda["fecha nacimiento"] = fat_panda["fecha nacimiento"].astype(str)
            fat_panda["estado civil"] = fat_panda["estado civil"].astype(str)
            for row in results:
                temp = list(row)
                temp[4] = '{0:%Y-%m-%d}'.format(temp[4])
                panda = pd.DataFrame([temp], columns= ["id", "nombre", "apellidos", "genero", "fecha nacimiento", "estado civil"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            clientes = []
            for index, row in fat_panda.iterrows():
                cliente = Cliente(row["nombre"], row["apellidos"],row["genero"], row["fecha nacimiento"], row["estado civil"],row["id"])
                clientes.append(cliente)
            return clientes[0]
        except:
            raise Exception("No se pudo extraer el cliente")
    def updatecliente(self,cliente):
        struct = "UPDATE Clientes SET Nombre = '%(nombre)s', Apellidos = '%(apellidos)s',Genero = '%(genero)s', Nacimiento = STR_TO_DATE('%(FN)s', '%(format)s') , EstadoCivil = '%(EC)s' WHERE Id = %(Id)d"
        data = {'nombre': cliente.getnombre(), 'apellidos': cliente.getapellidos(), 'genero':cliente.getgenero(),'FN':cliente.getFechaNacimiento(), 'format':"%Y-%m-%d" ,'EC':cliente.getEsteadoCivil(),'Id':cliente.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo actualizar el cliente")
    
    def createcliente(self,cliente):
        struct = "INSERT INTO Clientes (Nombre,Apellidos, Genero, Nacimiento, EstadoCivil) VALUES ('%(nombre)s','%(apellidos)s','%(genero)s',STR_TO_DATE('%(FN)s', '%(format)s'),'%(EC)s')"
        data = {'nombre': cliente.getnombre(), 'apellidos': cliente.getapellidos(), 'genero':cliente.getgenero(),'FN':cliente.getFechaNacimiento(), 'format':"%Y-%m-%d",'EC':cliente.getEsteadoCivil()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo crear el cliente")

    def destroycliente(self,cliente):
        struct = "DELETE FROM Clientes WHERE Id = %(Id)d"
        data = {'Id':cliente.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo destruir el cliente")

