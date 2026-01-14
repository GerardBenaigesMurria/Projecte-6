# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció:  Crea una classe Producte, Atributs: nom, preu, Mètode: aplicar un descompte (donat com a percentatge)
# Especificaicons de entrada: 

class producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu
    def descompte (self):
        print("Al producte",self.nom,"Descompte del 10%", self.preu * 0.9,"€")