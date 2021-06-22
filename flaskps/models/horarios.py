class Horario(object):

    db = None

    @classmethod
    def create(cls, t_r, nucleo, dia, inicio, fin):
        sql = """
            INSERT INTO `horarios`(`taller_responsable`, `nucleo_id`, `dia`, `inicio`, `fin`) 
            VALUES ( %s, %s, %s, %s, %s )
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,(t_r, nucleo, dia, inicio, fin) )
        cls.db.commit()
        return True

    @classmethod 
    def modificar(cls, idH, t_r, nucleo, dia, inicio, fin):
        sql = """
            UPDATE `horarios` 
            SET `taller_responsable`=%s,`nucleo_id`=%s,`dia`=%s,`inicio`=%s,`fin`=%s 
            WHERE id = %s 
            """
        cursor = cls.db.cursor()
        cursor.execute(sql,(t_r, nucleo, dia, inicio, fin, idH))
        cls.db.commit()
        return True

    @classmethod
    def borrar(cls, idH):
        sql = """ DELETE FROM `horarios` WHERE id = %s
        """
        cursor=cls.db.cursor()
        cursor.execute(sql,(idH))
        cls.db.commit()
        return cursor.fetchall()
    
    @classmethod
    def horariosDe(cls, idDrt):
        sql ="""
            SELECT * FROM `horarios` hs 
            INNER JOIN nucleo nc ON (hs.nucleo_id = nc.id)
            WHERE hs.taller_responsable = %s 
             """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idDrt))
        return cursor.fetchall() 
 
    @classmethod
    def buscarIdDrt(cls, docente, ciclo, taller):
        sql = """
            SELECT `id_drt` 
            FROM `docente_responsable_taller`
            WHERE ciclo_lectivo_id = %s AND taller_id = %s AND docente_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (ciclo, taller, docente))
        return cursor.fetchone()