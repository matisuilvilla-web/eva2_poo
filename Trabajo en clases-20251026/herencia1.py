class Vehiculo:
    #construtor
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    #metodo
    def mostrar_info(self):
        print(f"Marca {self.marca}, Modelo: {self.modelo}")

    def encender(self):
        print(f"{self.marca} {self.modelo} : está encendido")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo)
        self.anio = anio
    
    def mostrar_info(self):  #sobrecarga
        print(f"Marca {self.marca}, Modelo: {self.modelo}, Anio {self.anio}")

    def encender(self): #sobrecarga
        print(f"{self.marca} {self.modelo} : ruge al encenderse")

class Moto(Vehiculo):

    #como no hay atributos extras, nos sirve el constructor del padre
    #por lo que no debemos declararlo

    def encender(self):
        print(f"{self.marca} {self.modelo} : arranca con un rugido fuerte")


# Programa principal
#creando objetos, instancias
# vehiculo = Vehiculo("Subaru","impresa")
# auto = Auto("Lamborgini", "huracan", 2017)
# moto = Moto("Yamaha", "R1")

# #invocando metodos
# vehiculo.mostrar_info()
# vehiculo.encender()

# auto.mostrar_info()
# auto.encender()

# moto.mostrar_info()
# moto.encender()

vehiculos = [Vehiculo("Subaru","impresa"),
            Auto("Lamborgini", "huracan", 2017),
            Moto("Yamaha", "R1")]

for v in vehiculos:
    v.mostrar_info()
    v.encender()

