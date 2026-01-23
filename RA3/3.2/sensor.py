# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Sensor amb atribut privat __valor
# Especificaicons de entrada: 

class sensor:
    def __init__(self, valor):
        self.__valor = valor  

    def valor_get(self):
        return self.__valor

    def valor_set(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor

