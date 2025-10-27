#clase auto con 3 atributos

class Auto:
    def __init__ (self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

#Metodos getter
    def get_marca(self):
        return (self.marca)

    def get_modelo(self):
        return (self.modelo)
    
    def get_anio(self):
        return (self.anio)
    def get_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")
#Metodos setter
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo
#fin de la clase Auto

#crear un objeto
auto1 = Auto("Toyota", "mirai", 2015)
auto1.get_info()
auto1.set_modelo("Yaris")
auto1.get_info()
# print("auto1 modificado: ",auto1.marca, auto1.modelo, auto1.anio)
