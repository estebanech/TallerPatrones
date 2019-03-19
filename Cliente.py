from datetime import date
class Cliente:

    def __init__ (self, nombre, apellidos, genero, FN, EC, id = 0):
        self.__id = id
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__genero = genero
        self.__FNacimiento = FN
        self.__ECivil = EC
    
    def __str__(self):
        struct ="Id = %(Id)d, Nombre = %(nombre)s, Apellidos = %(apellidos)s,Genero = %(genero)s, Nacimiento = %(FN)s, EstadoCivil = %(EC)s"
        data = {'Id':self.__id, 'nombre': self.__nombre, 'apellidos': self.__apellidos, 'genero':self.__genero,'FN':self.__FNacimiento, 'EC':self.__ECivil}
        return struct % data
    
    def getid(self):
        return self.__id
    def getnombre(self):
        return self.__nombre
    def getapellidos(self):
        return self.__apellidos
    def getgenero(self):
        return self.__genero
    def getFechaNacimiento(self):
        return self.__FNacimiento
    def getEsteadoCivil(self):
        return self.__ECivil
    
    def setnombre(self,nombre):
        self.__nombre = nombre
    def setapellidos(self,apellidos):
        self.__apellidos = apellidos
    def setgenero(self,genero):
        self.__genero = genero
    def setFechaNacimiento(self,FN):
        self.__FNacimiento = FN
    def setEsteadoCivil(self, EC):
        self.__ECivil = EC
