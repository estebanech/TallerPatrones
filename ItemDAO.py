import pymysql
from DbConector import DbConector
from Item import Item
import pandas as pd
import datetime
class ItemDAO:
    def __init__(self):
        self.DB = DbConector.getInstancedb()
        self.DBconection = DbConector.getInstance()
    def getallitems(self):
        sql = """SELECT * FROM Items"""
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "idtipo", "descripcion", "valor"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["idtipo"] = fat_panda["idtipo"].astype(str)
            fat_panda["descripcion"] = fat_panda["descripcion"].astype(int)
            fat_panda["valor"] = fat_panda["valor"].astype(int)
            for row in results:
                temp = list(row)
                panda = pd.DataFrame([temp],columns=["id", "idtipo", "descripcion", "valor"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            return fat_panda
        except:
            raise Exception("No se pudo extraer los items")
    def getitemsbyid(self,id):
        sql = "SELECT * FROM Items WHERE Id = '%d'" % (id)
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "idtipo", "descripcion", "valor"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["idtipo"] = fat_panda["idtipo"].astype(str)
            fat_panda["descripcion"] = fat_panda["descripcion"].astype(int)
            fat_panda["valor"] = fat_panda["valor"].astype(int)
            for row in results:
                temp = list(row)
                panda = pd.DataFrame([temp],columns=["id", "idtipo", "descripcion", "valor"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
            return fat_panda
        except:
            raise Exception("No se pudo extraer el item")
    def updateitem(self,item):
        struct = "UPDATE Items SET IdTipo = %(idtipo)d, Descripcion = '%(descripcion)s',Valor = %(valor)s WHERE Id = %(Id)d"
        data = {'idtipo':item.getidtipo(), 'descripcion':item.getdescripcion() , 'valor':item.getvalor() ,'Id':item.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo actualizar el item")
    
    def createitem(self,item):
        struct = "INSERT INTO Items (IdTipo,Descripcion, Valor) VALUES (%(idtipo)s,'%(descripcion)s',%(valor)s)"
        data = {'idtipo':item.getidtipo(), 'descripcion':item.getdescripcion() , 'valor':item.getvalor()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo crear el item")

    def destroyitem(self,item):
        struct = "DELETE FROM Items WHERE Id = %(Id)d"
        data = {'Id':item.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo destuir el item")

