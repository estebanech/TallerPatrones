import pymysql
class DbConector:
    # Here will be the instance stored.
    __instance = None
    __database = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if DbConector.__instance == None:
            DbConector()
        return DbConector.__instance 
    
    @staticmethod
    def getInstancedb():
        """ Static access method. """
        if DbConector.__database == None:
            DbConector()
        return DbConector.__database 

    def __init__(self):
        """ Virtually private constructor. """
        if DbConector.__instance != None:
            raise Exception("Es una clase singleton!")
        else:
            db = pymysql.connect("localhost","esteban","rafa1997","tallerPatrones" )
            DbConector.__database = db
            DbConector.__instance = db.cursor()

