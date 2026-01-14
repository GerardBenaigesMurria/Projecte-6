# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció:Crea una classe Animal, Atributs: nom, espècie, Mètode fer_soroll() que mostri un text genèric (“fa un soroll”)
# Especificaicons de entrada: 

class animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie
    def fer_sorroll(self):
        print("Fa un soroll")