from modelos.proyecto import Proyecto
from db.database import Database

class ProyectoDAO:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self._create_table()

    def _create_table(self):
        """Crea la tabla de proyectos si no existe"""
        with self.database.connect() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS proyectos (
                                id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL,
                                descripcion TEXT,
                                fecha_inicio TEXT,
                                fecha_termino TEXT
                            )''')

    def insertar(self, proyecto):
        """Inserta un nuevo proyecto"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_termino)
                              VALUES (?, ?, ?, ?)''', 
                           (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_termino))
            conn.commit()
            proyecto.id_proyecto = cursor.lastrowid

    def seleccionar_todos(self):
        """Selecciona todos los proyectos"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM proyectos')
            registros = cursor.fetchall()
            return [Proyecto(id_proyecto=row[0], nombre=row[1], descripcion=row[2], 
                             fecha_inicio=row[3], fecha_termino=row[4]) for row in registros]

    def seleccionar_por_id(self, id_proyecto):
        """Selecciona un proyecto por su ID"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM proyectos WHERE id_proyecto = ?', (id_proyecto,))
            row = cursor.fetchone()
            if row:
                return Proyecto(id_proyecto=row[0], nombre=row[1], descripcion=row[2], 
                                fecha_inicio=row[3], fecha_termino=row[4])
            else:
                return None

    def actualizar(self, proyecto):
        """Actualiza un proyecto existente"""
        with self.database.connect() as conn:
            conn.execute('''UPDATE proyectos
                            SET nombre = ?, descripcion = ?, fecha_inicio = ?, fecha_termino = ?
                            WHERE id_proyecto = ?''',
                         (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_termino, proyecto.id_proyecto))
            conn.commit()

    def eliminar(self, id_proyecto):
        """Elimina un proyecto"""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM proyectos WHERE id_proyecto = ?', (id_proyecto,))
            conn.commit()
