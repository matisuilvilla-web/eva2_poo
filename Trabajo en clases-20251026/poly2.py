class Bebida:
    def servir(self):
        return "Sirviendo una bebida genérica"
    
class Cafe(Bebida):
    def servir(self):
        return "Sirviendo Cafe"

class Te(Bebida):
    def servir(self):
        return "Sirviendo Te"

#Funcion Polimorfica
def servir_bebida( Bebida ):
    #Llama al metodo servir() del objeto que le pasen
    return Bebida.servir()

#PP
cafecito = Cafe()
tecito = Te()
bebi = Bebida()

print(servir_bebida(tecito))