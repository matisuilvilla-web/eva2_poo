from db.database import Database
from modelos.empleado import Empleado


class EmpleadoDAO:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self._create_table()

    def _create_table(self):
        """Crea la tabla de empleados si no existe"""
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS empleados (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    direccion TEXT,
                    telefono TEXT,
                    email TEXT,
                    fecha_contrato TEXT,
                    salario REAL
                )
            ''')

    def insertar(self, empleado):
        """Inserta un nuevo empleado en la base de datos"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO empleados (nombre, direccion, telefono, email, fecha_contrato, salario) 
                              VALUES (?, ?, ?, ?, ?, ?)''', 
                           (empleado.nombre, empleado.direccion, empleado.telefono, 
                            empleado.email, empleado.fecha_contrato, empleado.salario))
            conn.commit()
            empleado.id_empleado = cursor.lastrowid

    def seleccionar_todos(self):
        """Obtiene todos los empleados de la base de datos"""
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM empleados')
            registros = cursor.fetchall()
            return [Empleado(id_empleado=row[0], nombre=row[1], direccion=row[2], telefono=row[3], 
                             email=row[4], fecha_contrato=row[5], salario=row[6]) for row in registros]

    def actualizar(self, empleado):
        """Actualiza los datos de un empleado"""
        with self.database.connect() as conn:
            conn.execute('''UPDATE empleados SET nombre = ?, direccion = ?, telefono = ?, email = ?, 
                            fecha_contrato = ?, salario = ? WHERE id_empleado = ?''', 
                         (empleado.nombre, empleado.direccion, empleado.telefono, empleado.email, 
                          empleado.fecha_contrato, empleado.salario, empleado.id_empleado))
            conn.commit()

    def eliminar(self, empleado_id):
        """Elimina un empleado por su ID"""
        with self.database.connect() as conn:
            conn.execute('DELETE FROM empleados WHERE id_empleado = ?', (empleado_id,))
            conn.commit()
