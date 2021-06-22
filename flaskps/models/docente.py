class Docente(object):

    db = None

#Crear docente
    @classmethod
    def create(cls, apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel, email):
        sql = """
            INSERT INTO `docente`(`apellido`, `nombre`, `fecha_nac`, `localidad_id`, `domicilio`, `tipo_doc_id`, `numero`, `tel`, `email`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel, email) )
        cls.db.commit()
        return True

    @classmethod
    def idDe(cls,user):
        sql = """SELECT `id` FROM `docente` WHERE `email` = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(user))
        return cursor.fetchone()

#Buscar en docente
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM docente'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def apiDocentes(cls):
        sql = 'SELECT id, nombre, apellido FROM docente'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def buscarId(cls, idD):
        sql = """
            SELECT * FROM docente AS e
            WHERE e.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idD))
        return cursor.fetchone()

    @classmethod
    def buscarEmail(cls, email):
        sql = """
            SELECT * FROM docente AS e
            WHERE e.email=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchone()

#Modificar docente
    @classmethod
    def modificar(cls, idD, apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel, email):
        sql = """
            UPDATE `docente` 
            SET  `apellido`= %s, `nombre`= %s, `fecha_nac`= %s, `localidad_id`= %s, 
                 `domicilio`= %s, `tipo_doc_id`= %s ,`numero`= %s ,`tel`= %s,`email`= %s
            WHERE id = %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(apellido, nombre, fecha_nac, localidad_id, domicilio, tipo_doc_id, numero, tel, email, idD))
        cls.db.commit()
        return True

    @classmethod
    def modificarUser(cls, emailPrev, apellido, nombre, email):
        sql = """
            UPDATE `docente` 
            SET  `apellido`= %s, `nombre`= %s, `email`= %s
            WHERE email = %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(apellido, nombre, email, emailPrev))
        cls.db.commit()
        return True

#borrar docente
    @classmethod
    def borrarDocente(cls,idD):
        sql = """ DELETE FROM `docente` WHERE `id`=%s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idD))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeTalleres(cls,idDocente):
        sql = """DELETE FROM `docente_responsable_taller` WHERE docente_id = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idDocente))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def talleresDe(cls,idDocente):
        sql ="""SELECT * FROM `docente_responsable_taller` drt 
                INNER JOIN taller t ON (t.id = drt.taller_id) 
                WHERE docente_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idDocente))
        return cursor.fetchall() 