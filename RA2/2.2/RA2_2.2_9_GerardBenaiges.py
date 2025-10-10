# Autor: Gerard Benaiges Murria
# Data: 10/10/2025
# Versió: 1
# Descripció: Trobar el nombre més gran d'una llista
# Especificacions de entrada: ficar una llista de números eterers separats per espais

llista = list(map(int, input("Introdueix una llista de numeros separats per espais: ").split()))

max = llista[0]

for numero in llista:
    if numero > max:
        max = numero

print("El nombre més gran és", max)