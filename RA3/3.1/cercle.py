# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Cercle, Atribut: radi, Mètodes: calcular àrea i perímetre
# Especificaicons de entrada: 

class cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        print("L'area és: ", 3.141592 * self.radi ** 2)
    
    def perimetre(self):
        print("El perimetre és: ", 2 * 3.141592 * self.radi)
    
        