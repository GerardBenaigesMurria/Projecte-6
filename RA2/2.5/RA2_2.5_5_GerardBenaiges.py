# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: La funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>"
# Especificacions de entrada: ficar una cadena de caracters

nom = str(input("Fica el teu nom "))

def saluda_nom():
    if len(nom) == 0:
        print("Hola, amic ")
    else:
        print (f"Hola, {nom}")

saluda_nom()