# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Ús del mòdul random, Escriu un programa que simuli llençar un dau (1-6) usant el mòdul random. Prova de fer una funció que llenci el dau n vegades i mostri la mitjana.
# Especificacions de entrada: ficar un numero enter

import random

def llançar_dau():
    total = 0
    for i in range(100):
        num = random.randint(1, 6)
        total += num
    mediana = total / 100
    return mediana

print("La mitjana és", llançar_dau())