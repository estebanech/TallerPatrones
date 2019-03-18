class TipoItem:

    def __init__ (self, descripcion, id = 0):
        self.__id = id
        self.__descripcion = descripcion
    
    def getid(self):
        return self.__id
    def getdescripcion(self):
        return self.__descripcion
    
    def setdescripcion(self,descripcion):
        self.__descripcion = descripcion