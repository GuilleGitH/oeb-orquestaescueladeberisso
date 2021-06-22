class Ciclo_lectivo(object):

    db = None

#Crear ciclo_lectivo
    @classmethod
    def create(cls, fecha_ini, fecha_fin, semestre, año):
        sql = """
            INSERT INTO `ciclo_lectivo`(`fecha_ini`, `fecha_fin`, `semestre`, `year`) VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(fecha_ini , fecha_fin , semestre, año) )
        cls.db.commit()
        return True

#Buscar en ciclo_lectivo
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM ciclo_lectivo'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
        
#buscar
    @classmethod 
    def buscar(cls, año, semestre):
        sql = """
            SELECT * FROM ciclo_lectivo
            WHERE semestre = %s AND year = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (semestre, año))
        return cursor.fetchone()

    @classmethod
    def buscarId(cls, idC):
        sql = """
            SELECT * FROM ciclo_lectivo
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idC))
        return cursor.fetchone()

    @classmethod
    def buscarTallerCiclo(cls, ciclo, taller):
        sql = """
            SELECT * FROM ciclo_lectivo_taller 
            WHERE taller_id = %s AND ciclo_lectivo_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller, ciclo))
        return cursor.fetchone()

#Modificar ciclo_lectivo no Anda
    @classmethod
    def modificar(cls,fecha_ini, fecha_fin, semestre, año):
        sql = """
            UPDATE `ciclo_lectivo` 
            SET  `fecha_ini`= %s, `fecha_fin`= %s, `semestre`= %s, `year`= %s 
            WHERE 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(fecha_ini, fecha_fin, semestre, año))
        cls.db.commit()
        return True

#borrar ciclo
    @classmethod
    def borrar(cls,fecha_ini, fecha_fin, semestre, año):
        sql = """ 
            DELETE FROM `ciclo_lectivo`  
            WHERE `fecha_ini`= %s, `fecha_fin`= %s, `semestre`= %s, , `year`= %s 
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(fecha_ini, fecha_fin, semestre, año))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeDocentes(cls,idC):
        sql = """DELETE FROM `docente_responsable_taller` WHERE ciclo_lectivo_id = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idC))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeEstudiantes(cls,idC):
        sql = """DELETE FROM `estudiante_taller` WHERE ciclo_lectivo_id = %s """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idC))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeCiclos(cls,idC):
        sql = """DELETE FROM `ciclo_lectivo_taller` WHERE ciclo_lectivo_id = %s """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idC))
        cls.db.commit()
        return cursor.fetchall()

#AgregarTallerACiclo
    @classmethod
    def agregarTaller(cls, taller_id, ciclo_id):
        sql = """
                INSERT INTO `ciclo_lectivo_taller`(`taller_id`, `ciclo_lectivo_id`) 
                VALUES (%s , %s )
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(taller_id,ciclo_id))
        cls.db.commit()
        return True