from modelos.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, idUsuario, username, password, rol, estado, nivelAcceso):
        super().__init__(idUsuario, username, password, rol, estado)
        self._nivelAcceso = nivelAcceso

    @property
    def nivelAcceso(self):
        return self._nivelAcceso

    @nivelAcceso.setter
    def nivelAcceso(self, valor):
        if valor < 0:
            raise ValueError("El nivel de acceso debe ser un número positivo.")
        self._nivelAcceso = valor

    def __str__(self):
        """Método para representar al Administrador en un formato legible."""
        return f"Administrador: {self.username}, Nivel de Acceso: {self._nivelAcceso}, Estado: {self.estado}"
