# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Sensor amb atribut privat __valor
# Especificaicons de entrada: 

class sensor:
    def __init__(self, valor):
        self.valor = valor  

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor

