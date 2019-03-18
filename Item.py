from TipoItemDAO import TipoItemDAO 
class Item:

    def __init__ (self, idtipo, descripcion, valor, id = 0):
        self.__id = id
        self.__descripcion = descripcion
        self.__valor = valor
        self.__idtipo = idtipo
    
    def getid(self):
        return self.__id
    def getdescripcion(self):
        return self.__descripcion
    def getvalor(self):
        return self.__valor
    def getidtipo(self):
        return self.__idtipo
    
    def setdescripcion(self,nombre):
        self.__descripcion = descripcion
    def setvalor(self,valor):
        self.__valor =  valor
    def setidtipo(self,idtipo):
        self.__idtipo = idtipo
