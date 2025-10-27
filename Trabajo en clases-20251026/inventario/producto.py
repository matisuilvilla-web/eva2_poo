# producto.py
class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self._codigo = None
        self._nombre = None
        self._precio = None
        self._stock = None

        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_precio(precio)
        self.set_stock(stock)

    # GETTERS
    def get_codigo(self): return self._codigo
    def get_nombre(self): return self._nombre
    def get_precio(self): return self._precio
    def get_stock(self):  return self._stock

    # SETTERS con validación simple
    def set_codigo(self, codigo: str):
        if not codigo or not codigo.strip():
            raise ValueError("El código no puede estar vacío")
        self._codigo = codigo.strip()

    def set_nombre(self, nombre: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    def set_precio(self, precio: float):
        try:
            precio = float(precio)
        except:
            raise ValueError("El precio debe ser numérico")
        if precio <= 0:
            raise ValueError("El precio debe ser > 0")
        self._precio = precio

    def set_stock(self, stock: int):
        try:
            stock = int(stock)
        except:
            raise ValueError("El stock debe ser entero")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = stock

    def mostrar_info(self):
        # miles con punto, sin depender de locale:
        precio_fmt = f"{self._precio:,.0f}".replace(",", ".")
        return f"[{self._codigo}] {self._nombre} - ${precio_fmt} - stock: {self._stock}"
