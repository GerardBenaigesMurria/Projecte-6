# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció:
# Especificaicons de entrada: 


class CarretCompra:
    def __init__(self, total): 
        self.total = total
    
    def preu_final(self, total):
        return self.total.aplicar(total)

class Descompte20:
    def aplicar(self, total):
        return total * 0.8
    
carretcompra = CarretCompra(Descompte20())
print(carretcompra.preu_final(100))