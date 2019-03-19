from datetime import date
class Factura:

    def __init__ (self, fecha, idcliente, estado, valor = 0,id = 0):
        self.__id = id
        self.__fecha = fecha
        self.__idcliente = idcliente
        self.__estado = estado
        self.__valor = valor
    
    def __str__ (self):
        struct ="Id = %(Id)d, Fecha = %(fecha)s, IdCliente = %(idcliente)d, Estado = %(estado)s, Valor = %(valor)d"
        data = {'Id':self.__id, 'fecha': self.__fecha, 'idcliente': self.__idcliente, 'estado':self.__estado,'valor':self.__valor}
        return struct % data
    
    def getid(self):
        return self.__id
    def getfecha(self):
        return self.__fecha
    def getidcliente(self):
        return self.__idcliente
    def getestado(self):
        return self.__estado
    def getvalor(self):
        return self.__valor
    
    def setfecha(self,fecha):
        self.__fecha = fecha
    def setidcliente(self,idcliente):
        self.__idcliente = idcliente
    def setestado(self,estado):
        self.__estado = estado
    def setvalor(self,valor):
        self.__valor = valor