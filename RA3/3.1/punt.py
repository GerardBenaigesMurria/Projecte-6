# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Punt, Atributs: x, y, Mètode: calcular la distància a un altre punt

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, altre_punt):
        print ("La distancia és:",(self.x**2 + self.y**2)**0.5)