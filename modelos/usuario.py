import bcrypt

class Usuario:
    def __init__(self, id_usuario, nombre, email, telefono, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = contraseña  # Recibimos la contraseña tal como la ingresan
        self.rol = rol

    def hash_password(self):
        """Genera un hash seguro de la contraseña usando bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(self.password.encode('utf-8'), salt)

    def check_password(self, password):
        """Verifica si la contraseña proporcionada coincide con el hash almacenado"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))