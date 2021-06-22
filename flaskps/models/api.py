class Api(object):

    db = None

#Recuperacion de Select
    #Tabla de genero
    @classmethod
    def generos(cls):
        sql = "SELECT * FROM `genero`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    #Persona a Cargo
    @classmethod
    def responsable(cls):
        sql = "SELECT * FROM `responsable`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    #Escuela
    @classmethod
    def escuela(cls):
        sql = "SELECT * FROM `escuela`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    #Barrio
    @classmethod
    def barrio(cls):
        sql = "SELECT * FROM `barrio`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def nivel(cls):
        sql = "SELECT * FROM `nivel`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def nucleos(cls):
        sql = "SELECT * FROM `nucleo`"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()