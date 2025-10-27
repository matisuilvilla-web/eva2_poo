from modelos.departamento import Departamento
from db.database import Database 

class DepartamentoDAO:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self._create_table()

    def _create_table(self):
        """Crea la tabla de departamentos si no existe"""
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS departamentos (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_depto TEXT NOT NULL,
                    gerente_id INTEGER,
                    FOREIGN KEY(gerente_id) REFERENCES empleados(id_empleado)
                )
            ''')

    def insertar(self, departamento):
        """Inserta un nuevo departamento"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO departamentos (nombre_depto, gerente_id)
                              VALUES (?, ?)''', 
                           (departamento.nombre_depto, departamento.gerente_id))
            conn.commit()
            departamento.id_departamento = cursor.lastrowid

    def seleccionar_todos(self):
        """Selecciona todos los departamentos"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM departamentos')
            registros = cursor.fetchall()
            return [Departamento(id_departamento=row[0], nombre_depto=row[1], gerente_id=row[2]) for row in registros]

    def actualizar(self, departamento):
        """Actualiza un departamento existente"""
        with self.database.connect() as conn:
            conn.execute('''UPDATE departamentos
                            SET nombre_depto = ?, gerente_id = ?
                            WHERE id_departamento = ?''',
                         (departamento.nombre_depto, departamento.gerente_id, departamento.id_departamento))
            conn.commit()

    def eliminar(self, id_departamento):
        """Elimina un departamento"""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM departamentos WHERE id_departamento = ?', (id_departamento,))
            conn.commit()
