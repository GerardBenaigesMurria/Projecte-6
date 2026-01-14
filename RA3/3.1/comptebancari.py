# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe CompteBancari, Atributs: saldo, Mètodes: ingressar, retirar, veure saldo
# Especificaicons de entrada: 

class comptebancari:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def ingressar (self):
        ingres = int(input("Quant vols ingressar "))
        self.saldo = ingres + self.saldo 
    
    def retirar (self):
        retirar = int(input("Quant vols retirar "))
        self.saldo = retirar - self.saldo 

    def veuresaldo(self):
        print(self.saldo)
