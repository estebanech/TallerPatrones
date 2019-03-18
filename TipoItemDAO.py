import pymysql
from DbConector import DbConector
from TipoItem import TipoItem
import pandas as pd
import datetime
class TipoItemDAO:
    def __init__(self):
        self.DB = DbConector.getInstancedb()
        self.DBconection = DbConector.getInstance()

    def getalltipoitem(self):
        sql = """SELECT * FROM TipoItem"""
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "descripcion"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["descripcion"] = fat_panda["descripcion"].astype(str)
            for row in results:
                temp = list(row)
                panda = pd.DataFrame([temp], columns=["id", "descripcion"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            return fat_panda
        except:
            raise Exception("No se pudo extraer los tipoitem")
            
    def gettipoitembyid(self,id):
        sql = "SELECT * FROM TipoItem WHERE Id = '%d'" % (id)
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "descripcion"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["descripcion"] = fat_panda["descripcion"].astype(str)
            for row in results:
                temp = list(row)
                panda = pd.DataFrame([temp], columns=["id", "descripcion"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            return fat_panda
        except:
            raise Exception("No se pudo extraer el tipoitem")

    def updatetipoitem(self,tipoitem):
        struct = "UPDATE TipoItem SET Descripcion = '%(descripcion)s' WHERE Id = %(Id)d"
        data = {'descripcion': tipoitem.getdescripcion(),'Id':tipoitem.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo actualizar el tipoitem")

    
    def createtipoitem(self,tipoitem):
        struct = "INSERT INTO TipoItem (Descripcion) VALUES ('%(descripcion)s')"
        data = {'descripcion':tipoitem.getdescripcion()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo crear el tipoitem")

    def destroytipoitem(self,tipoitem):
        struct = "DELETE FROM TipoItem WHERE Id = %(Id)d"
        data = {'Id':tipoitem.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo destuir el tipoitem")


