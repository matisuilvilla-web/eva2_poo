# Aquí está el cambio grande: en vez de manejar lista y CSV, 
# ahora usamos mysql.connector y consultas SQL.
# inventario.py
import mysql.connector
from db_producto import Producto

class Inventario:
    def __init__(self):
        # Conexión indicada por ti
        self.conexion = mysql.connector.connect(
            host="127.0.0.1",  # en Windows es mejor 127.0.0.1 que 'localhost'
            user="root",
            # password="tu_clave",
            database="test",
            # Si tu MySQL usa 3307, descomenta la línea siguiente:
            # port=3307,
        )

    # CREATE
    def crear(self, nombre, precio, stock):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, stock))
        self.conexion.commit()
        nuevo_id = cursor.lastrowid  # ID autoincremental asignado por MySQL
        cursor.close()
        return Producto(nuevo_id, nombre, precio, stock)

    # READ (lista completa)
    def listar(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM producto ORDER BY id")
        registros = cursor.fetchall()
        cursor.close()

        productos = []
        for fila in registros:
            p = Producto(fila[0], fila[1], fila[2], fila[3])
            productos.append(p)
        return productos

    # READ (uno por id)
    def buscar(self, id_):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM producto WHERE id = %s", (id_,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Producto(fila[0], fila[1], fila[2], fila[3])
        return None

    # UPDATE (acepta campos opcionales)
    def actualizar(self, id_, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
        p = self.buscar(id_)
        if p is None:
            raise LookupError("Producto no encontrado")

        if nuevo_nombre is not None and nuevo_nombre.strip():
            p.set_nombre(nuevo_nombre)
        if nuevo_precio is not None:
            p.set_precio(nuevo_precio)
        if nuevo_stock is not None:
            p.set_stock(nuevo_stock)

        cursor = self.conexion.cursor()
        sql = "UPDATE producto SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        cursor.execute(sql, (p.get_nombre(), p.get_precio(), p.get_stock(), id_))
        self.conexion.commit()
        cursor.close()
        return p

    # DELETE
    def eliminar(self, id_):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM producto WHERE id = %s", (id_,))
        self.conexion.commit()
        cursor.close()
        return True
