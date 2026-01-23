# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Classe Usuari amb atribut privat __contrasenya
# Especificaicons de entrada: 

class usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya
    
    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) > 8:
            self.__contrasenya = nova_contrasenya

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau
    