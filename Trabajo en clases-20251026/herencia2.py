class Persona:
    def __init__ (self, rut , nombre):
        self.rut = rut
        self.nombre = nombre

    
    def presentarse(self):
        return f"Soy {self.nombre} Rut: {self.rut}"

class Estudiante(Persona):
    def __init__(self, rut, nombre, carrera):
        super().__init__(rut, nombre )
        self.carrera = carrera
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base} Estudio {self.carrera}"

class Docente(Persona):
    def __init__(self, rut, nombre, asignatura):
        super().__init__(rut, nombre )
        self.asignatura = asignatura
    
    def presentarse(self):
        base = super().presentarse()
        return f"{base} Soy docente de {self.asignatura}"

#PP
per = Persona("4490789-K", "Claudia Salinas")
est = Estudiante ("20.324.718-0", "Zacarias Flores de la plaza", "Analista Programador")
doc = Docente("10.048123-6", "Elba Lazo", "POOS")

print(per.presentarse())
print(est.presentarse())
print(doc.presentarse())
