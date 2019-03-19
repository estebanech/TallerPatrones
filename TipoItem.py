class TipoItem:

    def __init__ (self, descripcion, id = 0):
        self.__id = id
        self.__descripcion = descripcion
    
    def __str__(self):
        struct ="Id = %(Id)d, Descripcion = %(descripcion)s"
        data = {'Id':self.__id, 'descripcion': self.__descripcion}
        return struct % data
    
    def getid(self):
        return self.__id
    def getdescripcion(self):
        return self.__descripcion
    
    def setdescripcion(self,descripcion):
        self.__descripcion = descripcion
