# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Crea una classe Termostat amb un atribut privat __temperatura
# Especificaicons de entrada: 

class termostat:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor


