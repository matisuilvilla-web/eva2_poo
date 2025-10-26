# Este archivo queda casi igual: define la clase Producto. 
#      No necesita cambios para BD.
# producto.py
class Producto:
    def __init__(self, id_, nombre, precio, stock):
        # id_ puede venir como None al crear (DB lo asigna)
        self._id = id_
        self._nombre = None
        self._precio = None
        self._stock = None

        self.set_nombre(nombre)
        self.set_precio(precio)
        self.set_stock(stock)

    # GETTERS
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_precio(self): return self._precio
    def get_stock(self):  return self._stock

    # SETTERS simples
    def set_id(self, nuevo_id):
        if nuevo_id is not None:
            self._id = int(nuevo_id)

    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    def set_precio(self, precio):
        try:
            precio = float(precio)
        except:
            raise ValueError("El precio debe ser numérico")
        if precio <= 0:
            raise ValueError("El precio debe ser > 0")
        self._precio = precio

    def set_stock(self, stock):
        try:
            stock = int(stock)
        except:
            raise ValueError("El stock debe ser entero")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = stock

    def mostrar_info(self):
        # Formato simple (2 decimales)
        return f"[{self._id}] {self._nombre} - ${self._precio:.2f} - stock: {self._stock}"
