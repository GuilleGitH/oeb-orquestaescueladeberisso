class Asistencia(object):

    db = None

    @classmethod
    def create(cls, id_taller_asist, fecha, estado, estudiante):
        sql = """
            INSERT INTO `asistencias`(`id_taller_asist`, `fecha`, `estado`, `estudiante`) 
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(id_taller_asist, fecha, estado, estudiante) )
        cls.db.commit()
        return True

    @classmethod
    def modificar(cls, horario, fecha, estado, estudiante):
        sql = """
            UPDATE `asistencias` 
            SET `estado` = %s 
            WHERE `id_taller_asist`= %s AND `fecha` = %s AND `estudiante` = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(estado, horario, fecha, estudiante))
        cls.db.commit()
        return True

    @classmethod
    def buscarAsistencia(cls, id_taller_asist, fecha, estudiante):
        sql = """
            SELECT * 
            FROM `asistencias` 
            WHERE `id_taller_asist`= %s AND `fecha` = %s AND `estudiante` = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(id_taller_asist, fecha, estudiante))
        return cursor.fetchone()

    @classmethod
    def horariosTallerDocente(cls, id_drt):
        sql = """
            SELECT * FROM `horarios` ho
            INNER JOIN docente_responsable_taller drt ON (ho.taller_responsable = drt.id_drt)
            INNER JOIN ciclo_lectivo cl ON (cl.id = drt.ciclo_lectivo_id)
            WHERE drt.id_drt = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_drt))
        return cursor.fetchall()

    @classmethod
    def diasTallerDocente(cls, id_drt):
        sql = """
            SELECT DISTINCT ho.dia FROM `horarios` ho
            INNER JOIN docente_responsable_taller drt ON (ho.taller_responsable = drt.id_drt)
            INNER JOIN ciclo_lectivo cl ON (cl.id = drt.ciclo_lectivo_id)
            WHERE drt.id_drt = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_drt))
        return cursor.fetchall()
    
    @classmethod 
    def buscarTaller(cls, idDrt):
        sql = """
            SELECT * FROM docente_responsable_taller drt
            INNER JOIN ciclo_lectivo cl ON (drt.ciclo_lectivo_id = cl.id)
            INNER JOIN taller t ON (drt.taller_id = t.id)
            WHERE drt.id_drt = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idDrt))
        return cursor.fetchone()

    @classmethod
    def buscarEstudiantesAsist(cls, taller_id, ciclo_id, fecha):
        sql = """SELECT a.estado, e.id, e.nombre, e.apellido FROM estudiante_taller et
                 INNER JOIN estudiante e ON (et.estudiante_id = e.id)
                 RIGHT JOIN asistencias a ON (a.estudiante=e.id)
                 WHERE et.taller_id = %s AND et.ciclo_lectivo_id = %s AND a.fecha = %s """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, ciclo_id, fecha))
        return cursor.fetchall()