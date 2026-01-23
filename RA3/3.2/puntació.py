# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Joc amb atribut privat __puntuacio
# Especificaicons de entrada: 

class joc:
    def __init__(self):
        self.__puntuacio = 0

    def puntuacio(self):
        return self.__puntuacio

    def sumar_punts(self, punts):
        if punts < 0:
            raise ValueError("No es poden sumar punts negatius")
        self.__puntuacio += punts

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0
