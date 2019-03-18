from datetime import date
class Factura:

    def __init__ (self, fecha, idcliente, estado, id = 0):
        self.__id = id
        self.__fecha = fecha
        self.__idcliente = idcliente
        self.__estado = estado
    
    def getid(self):
        return self.__id
    def getfecha(self):
        return self.__fecha
    def getidcliente(self):
        return self.__idcliente
    def getestado(self):
        return self.__estado
    
    def setfecha(self,fecha):
        self.__fecha = fecha
    def setidcliente(self,idcliente):
        self.__idcliente = idcliente
    def setestado(self,estado):
        self.__estado = estado