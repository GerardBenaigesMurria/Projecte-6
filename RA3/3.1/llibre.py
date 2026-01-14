# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Llibre, Atributs: títol, autor, any, Mètode mostrar_info() per imprimir les dades
# Especificaicons de entrada: 

class llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any
    def mostrar_info(self):
        print("El titol és", self.titol ,"l'autor és", self.autor, "i a l'any", self.any)