class Persona:
    def __init__(self, id_persona, nombre, edad):
        self.id_persona = id_persona
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona[id={self.id_persona}, nombre={self.nombre}, edad={self.edad}]"

