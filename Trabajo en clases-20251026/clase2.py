#clase auto con 3 atributos

class Auto:
    color = ""
    def __init__ (self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


#Metodos getter

    def get_color(self):
        return (self.color)

    def get_marca(self):
        return (self.marca)

    def get_modelo(self):
        return (self.modelo)
    
    def get_anio(self):
        return (self.anio)

    def get_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}")

#Metodos setter
    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def set_marca(self, nueva_marca):
        self.marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def set_anio(self, nuevo_anio):
        self.anio = nuevo_anio



#fin de la clase Auto

#crear un objeto
auto1 = Auto("Toyota", "mirai", 2015)
auxiliar = input("Ingrese color: ")
auto1.set_color(auxiliar)
auto1.get_info()

auto2 = Auto("Hyundai", "Accent", 2022)
auto2.get_info()
# auto1.set_modelo("Yaris")
# auto1.get_info()
# print("auto1 modificado: ",auto1.marca, auto1.modelo, auto1.anio)
