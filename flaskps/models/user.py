from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, *args, **kwargs):
        self.id = None
        self.fisrtname = None
        self.lastname = None
        self.email = None
        self.password = None
        self.activo = None
        self.updated_at = None
        self.created_at = None

    db = None

# Crear usuario

    @classmethod
    def create(cls, firstname, lastname, email, password):
        sql = """
            INSERT INTO users (firstname, lastname, email, password)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (firstname, lastname, email, password))
        cls.db.commit()
        return True

    # Oauth Methods

    @classmethod
    def porEmail(cls, email):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        query = cursor.fetchone()
        user = User()
        user.id, user.firstname, user.lastname, user.activo, user.email, user.password, user.created_at, user.updated_at = query['id'], query[
            'firstname'], query['lastname'], query['activo'], query['email'], query['password'], query['created_at'], query['updated_at']
        return user

    @classmethod
    def porID(cls, id):
        sql = """
            SELECT * FROM users AS u
            WHERE u.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        query = cursor.fetchone()
        user = User()
        user.id, user.firstname, user.lastname, user.activo, user.email, user.password, user.created_at, user.updated_at = query['id'], query[
            'firstname'], query['lastname'], query['activo'], query['email'], query['password'], query['created_at'], query['updated_at']
        return user

# Buscar en users
    @classmethod
    def all(cls):
        sql = 'SELECT * FROM users'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def buscarConEstado(cls, nombre, estado):
        sql = 'SELECT * FROM users WHERE id > 0 '
        if estado:
            sql += ' AND activo = ' + estado
        if nombre:
            sql += " AND firstname LIKE '" + nombre + "%'"
            sql += " OR lastname LIKE '" + nombre + "%'"
            sql += " OR email LIKE '" + nombre + "%'"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def buscar(cls, nombre):
        sql = 'SELECT * FROM users WHERE id > 0 '
        if nombre:
            sql += " AND firstname LIKE '" + nombre + "%'"
        print(nombre)
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def buscarSearch(cls, params):
        sql = 'SELECT * FROM users WHERE id > 0 '
        if 'estado' in params:
            sql += ' AND activo = ' + params['estado']
        if 'nombre' in params:
            sql += " AND firstname LIKE '" + params['nombre'] + "%'"
            sql += " OR lastname LIKE '" + params['nombre'] + "%'"
            sql += " OR email LIKE '" + params['nombre'] + "%'"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def buscarSearch(cls, params):
        sql = """SELECT * FROM users WHERE id > 0 """
        if (('nombre' in params) and (not params['nombre'] == '')):
            sql += " AND firstname like '" + params['nombre'] + "%'"
        if (('apellido' in params) and (not params['apellido'] == '')):
            sql += " AND lastname like '" + params['apellido'] + "%'"
        if (('email' in params) and (not params['email'] == '')):
            sql += " AND email like '" + params['email'] + "%'"
        if (('estado' in params) and (not params['estado'] == '')):
            sql += " AND activo = " + params['estado']
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s AND u.password = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email, password))
        query = cursor.fetchone()
        user = User()
        user.id, user.firstname, user.lastname, user.activo, user.email, user.password, user.created_at, user.updated_at = query['id'], query[
            'firstname'], query['lastname'], query['activo'], query['email'], query['password'], query['created_at'], query['updated_at']
        return user

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchone()

    @classmethod
    def obtenerHash(cls, email):
        sql = """ SELECT `password` FROM `users` WHERE `email` = %s 
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        aux = cursor.fetchone()
        return aux

    @classmethod
    def idDe(cls, user):
        sql = """SELECT `id` FROM `users` WHERE `email` = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (user))
        return cursor.fetchone()

# Modificar users
    @classmethod
    def modificar(cls, firstname, lastname, email, emailPrevio):
        sql = """
            UPDATE `users` SET `firstname`= %s,`lastname`= %s,`email`= %s
            WHERE email = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql, (firstname, lastname, email, emailPrevio))
        cls.db.commit()
        return True

    @classmethod
    def cambiarContraseña(cls, email, contraseña):
        sql = """
            UPDATE `users` SET `password`= %s
            WHERE email = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql, (contraseña, email))
        cls.db.commit()
        return True

    @classmethod
    def activar(cls, idu):
        sql = 'UPDATE `users` SET `activo`= 1 WHERE id = %s'
        cursor = cls.db.cursor()
        cursor.execute(sql, (idu))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def desactivar(cls, idu):
        sql = 'UPDATE `users` SET `activo`= 0 WHERE id = %s'
        cursor = cls.db.cursor()
        cursor.execute(sql, (idu))
        cls.db.commit()
        return cursor.fetchall()

# Roles Y Permisos
    @classmethod
    def rolesAll(cls, email):
        sql = """
            SELECT r.id, r.nombre FROM users u 
            INNER JOIN usuario_tiene_rol utr ON (u.id=utr.usuario_id) 
            INNER JOIN rol r ON (utr.rol_id=r.id) WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchall()

    @classmethod
    def roles(cls, email):
        sql = """
            SELECT r.id FROM users u 
            INNER JOIN usuario_tiene_rol utr ON (u.id=utr.usuario_id) 
            INNER JOIN rol r ON (utr.rol_id=r.id) WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchall()

    @classmethod
    def rolesNom(cls, email):
        sql = """
            SELECT r.nombre FROM users u 
            INNER JOIN usuario_tiene_rol utr ON (u.id=utr.usuario_id) 
            INNER JOIN rol r ON (utr.rol_id=r.id) WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchall()

    @classmethod
    def permiso(cls, roles):
        sql = """
            SELECT p.nombre FROM rol r 
            INNER JOIN rol_tiene_permiso rtp ON (r.id=rtp.rol_id) 
            INNER JOIN permiso p ON (rtp.permiso_id=p.id) 
            WHERE 
        """
        aux = " ( "
        for rol in roles:
            if roles[0] == rol:
                aux += " r.id = " + str(rol['id'])
            else:
                aux += " OR r.id = " + str(rol['id'])
        aux += ")"
        sql += aux
        cursor = cls.db.cursor()
        cursor.execute(sql)
        aux = cursor.fetchall()
        return aux

    @classmethod
    def rolDefault(cls, id):
        sql = """
            INSERT INTO `usuario_tiene_rol`(`usuario_id`, `rol_id`) VALUES (%s, 0)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()
        return True

    @classmethod
    def rolDocente(cls, id):
        sql = """
            INSERT INTO `usuario_tiene_rol`(`usuario_id`, `rol_id`) VALUES (%s, 3)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()
        return True

# borrar usuario
    @classmethod
    def borrarUsuario(cls, email):
        sql = """ DELETE FROM `users` WHERE `email`= %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def borrarDeRoles(cls, idUsuario):
        sql = """DELETE FROM `usuario_tiene_rol` WHERE `usuario_id` = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idUsuario))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def actualizarPermisos(cls, user, agregar):
        # quita los roles
        sql = """ DELETE FROM `usuario_tiene_rol` WHERE usuario_tiene_rol.usuario_id = """ + \
            str(user['id'])
        cursor = cls.db.cursor()
        cursor.execute(sql)
        cls.db.commit()
        # ahora agrega roles
        if agregar:
            sql = """ INSERT INTO `usuario_tiene_rol`(`usuario_id`, `rol_id`) VALUES
            """
            aux = ''
            for q in agregar:
                aux += "(" + str(user['id']) + "," + q + " ) ,"
            aux2 = aux[:-1]
            sql += aux2
            cursor = cls.db.cursor()
            cursor.execute(sql)
            cls.db.commit()
        return cursor.fetchall()
