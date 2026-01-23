# Autor: Gerard Benaiges Murria
# Data: 21/01/2026
# Versió: 1
# Descripció: Crea una classe Estudiant amb un atribut protegit _nota.
# Especificaicons de entrada: 

class estudiant:
    def __init__(self, nota):
        self._nota = nota
    
    def consultar_nota(self):
        return self._nota
    
    def sumar(self,quantitat):
        self._nota = self._nota + quantitat

    def restar(self,quantitat):
        self._nota = self._nota - quantitat

