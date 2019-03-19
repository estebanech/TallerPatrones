from TipoItemDAO import TipoItemDAO 
from TipoItem import TipoItem
class Item:

    def __init__ (self, idtipo, descripcion, valor, id = 0):
        self.__id = id
        self.__idtipo = idtipo
        self.__descripcion = descripcion
        self.__valor = valor
    
    def __str__(self):
        tipoDAO = TipoItemDAO()
        tipo = tipoDAO.gettipoitembyid(self.__idtipo).getdescripcion()
        struct ="Id = %(Id)d, TipoItem = %(tipo)s, Descripcion = %(descripcion)s, Valor = %(valor)s"
        data = {'Id':self.__id, 'tipo': tipo, 'descripcion': self.__descripcion, 'valor':self.__valor}
        return struct % data
    
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
