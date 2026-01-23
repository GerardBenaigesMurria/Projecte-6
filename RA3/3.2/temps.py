# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Rellotge amb atribut __hores
# Especificaicons de entrada: 

class rellotge:
    def __init__(self,hores):
        self.__hores = hores

    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            raise ValueError("Les hores han d'estar entre 0 i 23")    

    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"    
    