# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Estudiant, Atributs: nom, nota, Mètode: dir si ha aprovat o no (nota ≥ 5)
# Especificaicons de entrada: 

class estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    def aprovat (self):
        if self.nota >= 5:
            print("L'alumne",self.nom,"ha aprovat amb un",self.nota)
        else:
            print("L'alumne",self.nom,"ha suspes amb un",self.nota)