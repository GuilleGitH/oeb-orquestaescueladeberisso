class Taller(object):

    db = None

#Crear Taller
    @classmethod
    def create(cls, nombre, nombre_corto):
        sql = """
            INSERT INTO `taller`(`nombre`, `nombre_corto`) 
            VALUES (%s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(nombre, nombre_corto) )
        cls.db.commit()
        return True

#Buscar en taller
    @classmethod
    def all(cls):
        sql = """SELECT t.*, cl.year, cl.semestre, clt.* FROM taller t
                 INNER JOIN ciclo_lectivo_taller clt ON (t.id = clt.taller_id)
                 INNER JOIN ciclo_lectivo cl ON (clt.ciclo_lectivo_id = cl.id)
            """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall() 

    @classmethod
    def buscarApi(cls):
        sql = """ SELECT * FROM taller """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def buscarEstudiantes(cls, taller_id, ciclo_id):
        sql = """SELECT id, nombre, apellido FROM estudiante_taller et
                 INNER JOIN estudiante e ON (et.estudiante_id = e.id)
                 WHERE et.taller_id = %s AND et.ciclo_lectivo_id = %s """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, ciclo_id))
        return cursor.fetchall()
    
    @classmethod
    def buscarEstudiantesNo(cls, taller_id, ciclo_id):
        sql = """SELECT DISTINCT id, nombre, apellido FROM estudiante e
                WHERE ! EXISTS 
                    (SELECT estudiante_id 
                    FROM estudiante_taller et
                    WHERE et.taller_id = %s AND et.ciclo_lectivo_id = %s AND e.id=et.estudiante_id)"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, ciclo_id))
        return cursor.fetchall()

    @classmethod
    def buscarDocentes(cls, taller_id, ciclo_id):
        sql = """SELECT id, nombre, apellido, drt.id_drt FROM docente_responsable_taller drt 
                INNER JOIN docente d ON (drt.docente_id = d.id)
                WHERE drt.taller_id = %s AND drt.ciclo_lectivo_id = %s """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, ciclo_id))
        return cursor.fetchall()

    @classmethod
    def buscarDocentesNo(cls, taller_id, ciclo_id):
        sql = """SELECT id, nombre, apellido FROM docente d
                 WHERE ! EXISTS(
                     SELECT drt.docente_id
                     FROM docente_responsable_taller drt 
                     WHERE drt.taller_id = %s AND drt.ciclo_lectivo_id = %s AND drt.docente_id = d.id) """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, ciclo_id))
        return cursor.fetchall()

    @classmethod
    def buscar(cls, nombre):
        sql = """
            SELECT * FROM taller AS t
            WHERE t.nombre like %s%
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre))
        return cursor.fetchone()

    @classmethod
    def buscarID(cls, tid):
        sql = """
            SELECT * FROM taller AS t
            WHERE t.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (tid))
        return cursor.fetchone()

    @classmethod
    def talleresDeCiclo(cls, ciclo_id):
        sql = """
                SELECT t.* FROM `ciclo_lectivo_taller` clt 
                INNER JOIN `taller` t ON (clt.taller_id = t.id)
                INNER JOIN  `ciclo_lectivo` cl ON (cl.id = clt.ciclo_lectivo_id)
                WHERE clt.ciclo_lectivo_id = %s
              """
        cursor=cls.db.cursor()
        cursor.execute(sql,(ciclo_id))
        return cursor.fetchall()

#Modificar ciclo_lectivo
    @classmethod
    def modificar(cls, idT, nombre, nombre_corto):
        sql = """
            UPDATE `taller` 
            SET  `nombre`= %s, `nombre_corto`= %s
            WHERE `id`= %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(nombre, nombre_corto, idT))
        cls.db.commit()
        return True

#borrar taller
    @classmethod
    def borrar(cls, idT):
        sql = """ DELETE FROM `taller` WHERE id = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idT))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeDocentes(cls,idT):
        sql = """DELETE FROM `docente_responsable_taller` WHERE taller_id = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idT))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeEstudiantes(cls,idT):
        sql = """DELETE FROM `estudiante_taller` WHERE taller_id = %s """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idT))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeCiclos(cls,idT):
        sql = """DELETE FROM `ciclo_lectivo_taller` WHERE taller_id = %s """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idT))
        cls.db.commit()
        return cursor.fetchall()

#DocenteATaller
    @classmethod
    def agregarDocenteATaller(cls,docente_id, ciclo_id, taller_id):
        sql = """
                INSERT INTO `docente_responsable_taller`(`docente_id`, `ciclo_lectivo_id`, `taller_id`) 
                VALUES (%s , %s, %s)
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(docente_id, ciclo_id, taller_id))
        cls.db.commit()
        return True

    @classmethod
    def borrarDocenteDeTaller(cls,docente_id, ciclo_id, taller_id):
        sql = """
                DELETE FROM `docente_responsable_taller`
                WHERE docente_id= %s AND ciclo_lectivo_id= %s AND taller_id= %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(docente_id, ciclo_id, taller_id))
        cls.db.commit()
        return True

#EstudianteATaller
    @classmethod
    def AgregarEstudianteATaller(cls,estudiante_id, ciclo_id, taller_id):
        sql = """
                INSERT INTO `estudiante_taller`(`estudiante_id`, `ciclo_lectivo_id`, `taller_id`) 
                VALUES (%s , %s, %s) 
            """ 
        cursor = cls.db.cursor()
        cursor.execute(sql,(estudiante_id, ciclo_id, taller_id))
        cls.db.commit()
        return True

    @classmethod
    def borrarEstudianteDeTaller(cls,estudiante_id, ciclo_id, taller_id):
        sql = """
                DELETE FROM `estudiante_taller` 
                WHERE estudiante_id= %s AND ciclo_lectivo_id= %s AND taller_id= %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(estudiante_id, ciclo_id, taller_id))
        cls.db.commit()
        return True

    @classmethod
    def listarEstudiantesTaller(cls , taller_id):
        sql= """
             SELECT * FROM `estudiante_taller` AS t INNER JOIN `estudiante` AS e 
             WHERE t.taller_id = %s AND e.id = t.estudiante_id
             """
        cursor = cls.db.cursor()
        cursor.execute(sql,(taller_id))
        return cursor.fetchall()

    @classmethod
    def listarDocentesTaller(cls , taller_id):
        sql= """
             SELECT * FROM `docente_responsable_taller` AS t INNER JOIN `docente` AS d 
             WHERE t.taller_id = %s AND d.id = t.docente_id
             """
        cursor = cls.db.cursor()
        cursor.execute(sql,(taller_id))
        return cursor.fetchall()
