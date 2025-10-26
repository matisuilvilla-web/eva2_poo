class CuentaBancaria:
    titular = None

    def __init__(self, numero, saldo_inicial):
        self._numero = numero
        self._saldo_inicial = saldo_inicial

    #Getters
    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo_inicial

    #Setters
    def set_numero(self, nuevo_numero):
        self._numero = nuevo_numero

    def set_saldo(self, nuevo_saldo):
        self._saldo_inicial = nuevo_saldo

    #Metodos
    def depositar(self, monto):
        self._saldo_inicial = self._saldo_inicial + monto
        print(f"Depositó: ${monto} y el nuevo saldo es: ${self._saldo_inicial}")
    
    def girar(self, monto):
        if self._saldo_inicial - monto >= 0:
            self._saldo_inicial = self._saldo_inicial - monto
            print(f"Giró  ${monto} y el nuevo saldo es: ${self._saldo_inicial}")
        else:
            print(f"Saldo insuficinte para girar ${monto}")

    def mostrar_saldo(self):
        print(f"El saldo en cuenta {self._numero} es ${self._saldo_inicial}")

#PP
cuenta = CuentaBancaria(123456, 1000)
cuenta.mostrar_saldo()
cuenta.depositar(5000)
cuenta.girar(2000)
cuenta.girar(7000)
# cuenta.mostrar_saldo()


