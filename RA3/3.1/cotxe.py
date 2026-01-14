# Autor: Gerard Benaiges Murria
# Data: 14/01/2026
# Versió: 1
# Descripció: Crea una classe Cotxe, Atributs: marca, model, any, Mètode per mostrar la informació del cotxe
# Especificaicons de entrada: 

class cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
    def descriure(self):
        print(f"Cotxe: {self.marca} {self.model} de l'any {self.any}")