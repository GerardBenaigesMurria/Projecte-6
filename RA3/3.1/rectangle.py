# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Rectangle, Atributs: amplada, alçada, Mètodes: area() i perimetre()
# Especificaicons de entrada: 

class rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada
    def area(self):
        print ("L'area és:", self.amplada * self.alçada)
    def perimetre(self):
        print (2 * (self.amplada + self.alçada))