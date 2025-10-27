from modelos.administrador import Administrador
from  db.database import Database

class AdministradorDAO:
    def __init__(self):
        self.database = Database()
        self._create_table()

    def _create_table(self):
        """Crea la tabla de administradores si no existe."""
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS administrador (
                    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    nivelAcceso INTEGER NOT NULL
                )
            ''')

    def insertar(self, administrador):
        """Inserta un nuevo administrador en la base de datos."""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO administrador (username, password, rol, estado, nivelAcceso)
                              VALUES (?, ?, ?, ?, ?)''', 
                           (administrador.username, administrador.password, administrador.rol, 
                            administrador.estado, administrador.nivelAcceso))
            conn.commit()
            administrador.idUsuario = cursor.lastrowid  # Establece el ID del administrador

    def seleccionar_todos(self):
        """Devuelve todos los administradores de la base de datos."""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM administrador')
            registros = cursor.fetchall()
            return [Administrador(idUsuario=row[0], username=row[1], password=row[2], 
                                  rol=row[3], estado=row[4], nivelAcceso=row[5]) for row in registros]

    def seleccionar_por_id(self, idUsuario):
        """Devuelve un administrador por su ID."""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM administrador WHERE idUsuario = ?', (idUsuario,))
            row = cursor.fetchone()
            if row:
                return Administrador(idUsuario=row[0], username=row[1], password=row[2], 
                                     rol=row[3], estado=row[4], nivelAcceso=row[5])
            return None

    def actualizar(self, administrador):
        """Actualiza los datos de un administrador existente."""
        with self.database.connect() as conn:
            conn.execute('''UPDATE administrador 
                            SET username = ?, password = ?, rol = ?, estado = ?, nivelAcceso = ? 
                            WHERE idUsuario = ?''', 
                         (administrador.username, administrador.password, administrador.rol,
                          administrador.estado, administrador.nivelAcceso, administrador.idUsuario))
            conn.commit()

    def eliminar(self, idUsuario):
        """Elimina un administrador de la base de datos."""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM administrador WHERE idUsuario = ?', (idUsuario,))
            conn.commit()
