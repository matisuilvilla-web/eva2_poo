# import sqlite3
from persona import Persona
from database import Database

class PersonaDAO:
    def __init__(self):
        self.database = Database()
        self._create_table()

    def _create_table(self):
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS persona (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL
                )
            ''')

    def insertar(self, persona):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO persona (nombre, edad) VALUES (?, ?)', 
                           (persona.nombre, persona.edad))
            conn.commit()
            persona.id_persona = cursor.lastrowid

    def seleccionar_todos(self):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM persona')
            registros = cursor.fetchall()
            return [Persona(id_persona=row[0], nombre=row[1], edad=row[2]) for row in registros]

    def actualizar(self, persona):
        with self.database.connect() as conn:
            conn.execute('''UPDATE persona 
                          SET nombre = ?, 
                             edad = ? 
                          WHERE id = ?''', 
                         (persona.nombre, persona.edad, persona.id_persona))
            conn.commit()

    def eliminar(self, persona_id):
        with self.database.connect() as conn:
            conn.execute('DELETE FROM persona WHERE id = ?', (persona_id,))
            conn.commit()
