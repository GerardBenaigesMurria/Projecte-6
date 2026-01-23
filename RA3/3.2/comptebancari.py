# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe amb el atribut __saldo privat
# Especificaicons de entrada: 

class compte_bancari:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo
    
    def ingressar(self,quantitat):
        self.__saldo = self.__saldo + quantitat
    
    def retirar(self,quantitat):
        self.__saldo = self.__saldo - quantitat