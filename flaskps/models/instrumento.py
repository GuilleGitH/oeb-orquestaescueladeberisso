class Instrumento(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT i.*, t.nombre AS nombreTipo FROM instrumento i INNER JOIN tipo_instrumento t ON ( t.id = i.tipo_id)'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def create(cls, nombre, tipo, n_inventario, latitud, longitud, id_alumno):
        sql = """
            INSERT INTO `instrumento`(`nombre`, `tipo_id`, `n_inventario`, `longitud`, `latitud`, `id_alumno`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, tipo, n_inventario,
                             longitud, latitud, id_alumno))
        cls.db.commit()
        return True

    @classmethod
    def find_by_numero(cls, n_inventario):
        sql = """
            SELECT * FROM instrumento AS i
            WHERE i.n_inventario = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (n_inventario))
        return cursor.fetchone()

    @classmethod
    def find_by_id(cls, n_inventario):
        sql = """
            SELECT i.*, e.localidad_id, e.domicilio FROM instrumento AS i
            LEFT JOIN estudiante e ON (i.id_alumno = e.id)
            WHERE i.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (n_inventario))
        return cursor.fetchone()

    @classmethod
    def borrarInstrumento(cls, instrumento_id):
        sql = """ DELETE FROM `instrumento` WHERE `id`= %s """
        cursor = cls.db.cursor()
        cursor.execute(sql, (instrumento_id))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def modificarInstrumento(cls, id_instrumento, nombre, tipo_id, n_inventario, longitud, latitud, id_alumno):
        sql = """
        UPDATE `instrumento` 
        SET `nombre`= %s ,`tipo_id`= %s ,`n_inventario`= %s ,`longitud`= %s ,`latitud`= %s ,`id_alumno`= %s  
        WHERE `id`= %s
              """
        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, tipo_id, n_inventario,
                             longitud, latitud, id_alumno, id_instrumento))
        cls.db.commit()
        return True
