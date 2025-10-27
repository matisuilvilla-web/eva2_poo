from modelos.usuario import Usuario  
from db.database import Database
import bcrypt
import sqlite3

class UsuarioDAO:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self._create_table()

    def _create_table(self):
        """Crea la tabla de usuarios si no existe"""
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    contraseña TEXT NOT NULL,
                    rol TEXT NOT NULL
                )
            ''')

    def insertar(self, usuario):
        """Inserta un nuevo usuario"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, email, telefono, contraseña, rol)
                              VALUES (?, ?, ?, ?, ?)''', 
                           (usuario.nombre, usuario.email, usuario.telefono, usuario.password, usuario.rol))
            conn.commit()
            usuario.id_usuario = cursor.lastrowid

    def autenticar(self, username, password):
        """Autentica al usuario con su nombre de usuario y contraseña"""
        query = "SELECT * FROM usuarios WHERE nombre = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (username,))
        usuario_data = cursor.fetchone()
        
        if usuario_data:
            # Si el usuario existe, verificamos la contraseña
            usuario = Usuario(*usuario_data)
            if usuario.check_password(password):  # Comprobamos que la contraseña coincida
                return usuario
        return None  # Si no existe o la contraseña es incorrecta, devolvemos None

    def seleccionar_todos(self):
        """Selecciona todos los usuarios"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuarios')
            registros = cursor.fetchall()
            return [Usuario(id_usuario=row[0], nombre=row[1], email=row[2], 
                            telefono=row[3], contraseña=row[4], rol=row[5]) for row in registros]

    def actualizar(self, usuario):
        """Actualiza un usuario existente"""
        with self.database.connect() as conn:
            conn.execute('''UPDATE usuarios
                            SET nombre = ?, email = ?, telefono = ?, contraseña = ?, rol = ?
                            WHERE id_usuario = ?''',
                         (usuario.nombre, usuario.email, usuario.telefono, usuario.contraseña, usuario.rol, usuario.id_usuario))
            conn.commit()

    def eliminar(self, id_usuario):
        """Elimina un usuario"""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM usuarios WHERE id_usuario = ?', (id_usuario,))
            conn.commit()

    def seleccionar_por_email(self, email):
        """Selecciona un usuario por su email (para login o validación)"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
            row = cursor.fetchone()
            if row:
                return Usuario(id_usuario=row[0], nombre=row[1], email=row[2], telefono=row[3], 
                               contraseña=row[4], rol=row[5])
            return None
