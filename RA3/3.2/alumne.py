# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Alumne amb atribut privat __edat
# Especificaicons de entrada: 

class alumne:
    def __init__(self, edat):
        self.__edat = edat
    
    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, valor):
        if valor >= 0:
            self.__edat = valor
        else:
            raise ValueError("L'edat no pot ser negativa")