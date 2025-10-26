# inventario.py
import csv
from producto import Producto

class Inventario:
    def __init__(self):
        self._items = []  # lista de Producto

    # CRUD
    def crear(self, codigo, nombre, precio, stock):
        if self.buscar(codigo) is not None:
            raise ValueError("Ya existe un producto con ese código")
        p = Producto(codigo, nombre, precio, stock)
        self._items.append(p)
        return p

    def listar(self):
        return list(self._items)

    def buscar(self, codigo):
        for p in self._items:
            if p.get_codigo() == codigo:
                return p
        return None

    def actualizar(self, codigo, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
        p = self.buscar(codigo)
        if p is None:
            raise LookupError("Producto no encontrado")
        if nuevo_nombre is not None:
            p.set_nombre(nuevo_nombre)
        if nuevo_precio is not None:
            p.set_precio(nuevo_precio)
        if nuevo_stock is not None:
            p.set_stock(nuevo_stock)
        return p

    def eliminar(self, codigo):
        p = self.buscar(codigo)
        if p is None:
            raise LookupError("Producto no encontrado")
        self._items.remove(p)
        return True

    # Persistencia CSV simple
    def cargar_desde_csv(self, ruta_csv="data.csv"):
        try:
            with open(ruta_csv, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self._items.clear()
                for row in reader:
                    self.crear(
                        row["codigo"],
                        row["nombre"],
                        float(row["precio"]),
                        int(row["stock"])
                    )
        except FileNotFoundError:
            # Si no existe el archivo, partimos con inventario vacío
            pass

    def guardar_a_csv(self, ruta_csv="data.csv"):
        with open(ruta_csv, mode="w", newline="", encoding="utf-8") as f:
            campos = ["codigo", "nombre", "precio", "stock"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for p in self._items:
                writer.writerow({
                    "codigo": p.get_codigo(),
                    "nombre": p.get_nombre(),
                    "precio": p.get_precio(),
                    "stock":  p.get_stock(),
                })
