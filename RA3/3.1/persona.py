# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Persona, Atributs: nom, edat, Mètode presentar_se() que imprimeixi “Hola, soc X i tinc Y anys”
# Especificaicons de entrada: 

class persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    def presentarse (self):
        print("hola soc",self.nom,"i tinc", self.edat,"anys")