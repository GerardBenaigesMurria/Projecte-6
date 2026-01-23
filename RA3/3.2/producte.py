# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Producte amb atributs: nom (públic), __preu (privat)
# Especificaicons de entrada: 

class producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu
    
    def consultar_preu(self):
        return self.__preu
    
    def modificar_preu(self,nou_preu):
        self.__preu = nou_preu

