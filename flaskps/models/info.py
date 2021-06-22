class Info(object):

    db = None
    
    @classmethod
    def obtener(cls):
        sql = 'SELECT * FROM informacion LIMIT 1'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def cambiarInfo(cls, titulo,descripcion,contacto,cantidadfilas, habilitado):
        sql = """
            UPDATE `informacion` SET `titulo`=%s , `descripcion`=%s , `contacto`=%s , `cantidadfilas`=%s, `habilitado`=%s
        """ 
        cursor = cls.db.cursor()
        aux = int(cantidadfilas)
        aux2 = int(habilitado)
        cursor.execute(sql, (titulo,descripcion,contacto,aux,aux2))
        cls.db.commit()
        return True

    @classmethod
    def deshabilitar(cls):
        sql = 'UPDATE `informacion` SET `habilitado`= 0'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        cls.db.commit()
        return cursor.fetchall()
    
    @classmethod
    def habilitar(cls):
        sql = 'UPDATE `informacion` SET `habilitado`= 1'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        cls.db.commit()
        return cursor.fetchall()