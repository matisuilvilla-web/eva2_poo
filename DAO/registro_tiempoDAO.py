from modelos.registro_tiempo import RegistroTiempo
from db.database import Database


class RegistroTiempoDAO:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self._create_table()

    def _create_table(self):
        """Crea la tabla de registros de tiempo si no existe"""
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS registros_tiempo (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER,
                    id_proyecto INTEGER,
                    horas_trabajadas REAL,
                    descripcion TEXT,
                    FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado),
                    FOREIGN KEY(id_proyecto) REFERENCES proyectos(id_proyecto)
                )
            ''')

    def insertar(self, registro_tiempo):
        """Inserta un nuevo registro de tiempo"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO registros_tiempo (id_empleado, id_proyecto, horas_trabajadas, descripcion)
                              VALUES (?, ?, ?, ?)''', 
                           (registro_tiempo.idEmpleado, registro_tiempo.idProyecto, 
                            registro_tiempo.horas_trabajadas, registro_tiempo.descripcion))
            conn.commit()
            registro_tiempo.id_registro = cursor.lastrowid

    def seleccionar_todos(self):
        """Selecciona todos los registros de tiempo"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM registros_tiempo')
            registros = cursor.fetchall()
            return [RegistroTiempo(id_registro=row[0], id_empleado=row[1], id_proyecto=row[2], 
                                   horas_trabajadas=row[3], descripcion=row[4]) for row in registros]

    def actualizar(self, registro_tiempo):
        """Actualiza un registro de tiempo existente"""
        with self.database.connect() as conn:
            conn.execute('''UPDATE registros_tiempo
                            SET id_empleado = ?, id_proyecto = ?, horas_trabajadas = ?, descripcion = ?
                            WHERE id_registro = ?''',
                         (registro_tiempo.id_empleado, registro_tiempo.id_proyecto, 
                          registro_tiempo.horas_trabajadas, registro_tiempo.descripcion, 
                          registro_tiempo.id_registro))
            conn.commit()

    def eliminar(self, id_registro):
        """Elimina un registro de tiempo"""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM registros_tiempo WHERE id_registro = ?', (id_registro,))
            conn.commit()
