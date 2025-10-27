import math

class Figura:
    def area(self):
        raise NotImplementedError("Debes implementar el método area() en la subclase")
    
    def perimetro(self):
        raise NotImplementedError("Debes implementar el método perimetro() en la subclase")

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        if ancho < 0 or alto < 0:
            raise ValueError("Dimensiones deben ser positivas")
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def describir(self):
        return f"Rectangulo {self.ancho} x {self.alto}"


class Circulo(Figura):
    def __init__(self, radio):
        if radio <= 0 :
            raise ValueError("El radio sebe ser positivo")
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return math.pi * self.radio * 2 

    def describir(self):
        return f"Circulo de r={self.radio}"
#PP
# fig = Figura()
# print(f"El area es {fig.area()}")
# r = Rectangulo(4,-3)
# print(f"El area es {r.area()}")
# print(r.describir())

cir = Circulo(10)
print(f"El area es : {cir.area()}") 
print(cir.describir()) 
