import pymysql
from DbConector import DbConector
from Factura import Factura
from ItemDAO import ItemDAO
from Item import Item
import pandas as pd
import datetime
class FacturaDAO:
    def __init__(self):
        self.DB = DbConector.getInstancedb()
        self.DBconection = DbConector.getInstance()
   
    def findvalor(self,id):
        valor = 0
        itemval = 0
        sqllist = "SELECT * FROM DetalleFactura WHERE IdFactura = %d" % (id)
        self.DBconection.execute(sqllist)
        details = self.DBconection.fetchall()
        for detail in details:
            temp2 = list(detail)
            if len(temp2)>0:
                itemDAO = ItemDAO()
                itemval = itemDAO.getitemsbyid(temp2[2]).getvalor()
            else:
                itemval = 0
            valor += itemval * temp2[3] 
        return valor

    def getallfacturas(self):
        sql = """SELECT * FROM Facturas"""
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "fecha", "idcliente", "estado","valor"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["fecha"] = fat_panda["fecha"].astype(str)
            fat_panda["idcliente"] = fat_panda["idcliente"].astype(int)
            fat_panda["estado"] = fat_panda["estado"].astype(str)
            fat_panda["valor"] = fat_panda["valor"].astype(int)
            valor = 0
            for row in results:
                temp = list(row)
                temp[1] = '{0:%Y-%m-%d}'.format(temp[1])
                valor = self.findvalor(temp[0])
                temp.append(valor)
                panda = pd.DataFrame([temp], columns=["id", "fecha", "idcliente", "estado","valor"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
                valor = 0
            facturas = []
            for index, row in fat_panda.iterrows():
                factura = Factura(row["fecha"], row["idcliente"],row["estado"], row["valor"], row["id"])
                facturas.append(factura)
            return facturas
        except:
            raise Exception("No se pudo extraer los facturas")
    def getfacturabyid(self,id):
        sql = "SELECT * FROM Facturas WHERE Id = '%d'" % (id)
        try:
            self.DBconection.execute(sql)
            results = self.DBconection.fetchall()
            fat_panda = pd.DataFrame(columns=["id", "fecha", "idcliente", "estado","valor"])
            fat_panda["id"] = fat_panda["id"].astype(int)
            fat_panda["fecha"] = fat_panda["fecha"].astype(str)
            fat_panda["idcliente"] = fat_panda["idcliente"].astype(int)
            fat_panda["estado"] = fat_panda["estado"].astype(str)
            fat_panda["valor"] = fat_panda["valor"].astype(int)
            valor = 0
            for row in results:
                temp = list(row)
                temp[1] = '{0:%Y-%m-%d}'.format(temp[1])
                valor = self.findvalor(temp[0])
                temp.append(valor)
                panda = pd.DataFrame([temp], columns=["id", "fecha", "idcliente", "estado","valor"])
                fat_panda = pd.concat([fat_panda,panda], ignore_index=True)
                valor = 0
            facturas = []
            for index, row in fat_panda.iterrows():
                factura = Factura(row["fecha"], row["idcliente"],row["estado"], row["valor"], row["id"])
                facturas.append(factura)
            return facturas[0]
        except:
            raise Exception("No se pudo extraer el factura")
    

    def updatefactura(self,factura):
        struct = "UPDATE Facturas SET Fecha = STR_TO_DATE('%(fecha)s', '%(format)s'), IdCliente = %(idcliente)d,Estado = '%(estado)s' WHERE Id = %(Id)d"
        data = {'fecha':factura.getfecha(), 'format':"%Y-%m-%d" ,'idcliente': factura.getidcliente(), 'estado': factura.getestado(), 'Id':factura.getid()}
        print(sql)
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo actualizar el factura")

    def additems(self,factura,items):
        id = factura.getid()
        struct = "INSERT INTO DetalleFactura (IdFactura,IdItem, Cantidad) VALUES (%(idfactura)d,%(iditem)d,%(cantidad)d)"
        try:
            for item in items:
                indexitem,cantidad = item
                data = {'idfactura': id , 'iditem':indexitem.getid(),'cantidad':cantidad}
                sql = struct % data
                self.DBconection.execute(sql)
                self.DB.commit()
            factura.setvalor(self.findvalor(factura.getid()))            
        except:
            self.DB.rollback()
            raise Exception("No se pudo añadir el item a la factura")

    
    def createfactura(self,factura):
        struct = "INSERT INTO Facturas (Fecha,IdCliente, Estado) VALUES (STR_TO_DATE('%(fecha)s', '%(format)s'),%(idcliente)d,'%(estado)s')"
        data = {'fecha':factura.getfecha(), 'format':"%Y-%m-%d" ,'idcliente': factura.getidcliente(), 'estado': factura.getestado()}
        sql = struct % data
        print(sql)
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo crear el factura")
    
    def destroyiteminfactura(self,factura,item):
        struct = "DELETE FROM DetalleFactura WHERE IdFactura = %(Id)d AND IdItem = %(IdItem)d"
        data = {'Id': factura.getid(),'IdItem': item.getid()}
        sql = struct % data
        try:
            self.DBconection.execute(sql)
            self.DB.commit()
            factura.setvalor(self.findvalor(factura.getid())) 
        except:
            self.DB.rollback()
            raise Exception("No se pudo destruir el factura")


    def destroyfactura(self,factura):         
        struct = "DELETE FROM Facturas WHERE Id = %(Id)d"
        struct2 = "DELETE FROM DetalleFactura WHERE IdFactura = %(Id)d"
        data = {'Id':factura.getid()}
        sql = struct % data
        sql2 = struct2 % data
        try:
            self.DBconection.execute(sql2)
            self.DB.commit()
            self.DBconection.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            raise Exception("No se pudo destruir el factura")

