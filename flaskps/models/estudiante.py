class Estudiante(object):

    db = None

#Crear estudiante
    @classmethod
    def create(cls, apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, lugar_nac, responsable):
        sql = """
            INSERT INTO `estudiante`(`apellido`, `nombre`, `fecha_nac`, `localidad_id`, `nivel_id`, `domicilio`, `genero_id`, `escuela_id`, `tipo_doc_id`, `numero`, `tel`, `barrio_id`, `lugar_nac`, `responsable`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, lugar_nac, responsable) )
        cls.db.commit()
        return True 

#Buscar en estudiante
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM estudiante'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def apiEstudiantes(cls):
        sql = 'SELECT id, nombre, apellido FROM estudiante'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def buscarId(cls, idE):
        sql = """
            SELECT * FROM estudiante AS e
            WHERE e.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idE))
        return cursor.fetchone()

#Modificar estudiante
    @classmethod
    def modificar(cls, idE, apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, lugar_nac, responsable):
        sql = """
            UPDATE `estudiante` 
            SET  `apellido`= %s, `nombre`= %s, `fecha_nac`= %s, `localidad_id`= %s, 
                 `nivel_id`= %s, `domicilio`= %s, `genero_id`= %s, `escuela_id`= %s,
                 `tipo_doc_id`= %s ,`numero`= %s ,`tel`= %s ,`barrio_id`= %s, `lugar_nac`= %s, `responsable`= %s 
            WHERE id = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, lugar_nac, responsable, idE))
        cls.db.commit()
        return True

#borrar estudiante
    @classmethod
    def borrarEstudiante(cls,idU):
        sql = """ DELETE FROM `estudiante` WHERE `id`=%s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idU))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeTalleres(cls,idEstudiante):
        sql = """DELETE FROM `estudiante_taller` WHERE estudiante_id = %s """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idEstudiante))
        cls.db.commit()
        return cursor.fetchall()