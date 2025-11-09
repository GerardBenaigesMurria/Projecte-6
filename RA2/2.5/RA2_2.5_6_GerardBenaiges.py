# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació
# Especificacions de entrada: ficar un numero enter

num_nombres = int(input("Introdueix una quantitat de nombres "))
numeros = [int(input("Introdueix un numero ")) for i in range(num_nombres)]


def multiplica_tot(numeros):
    suma_total = 0
    i = 0
    while i < num_nombres:
        if i == 0:
            suma_total = numeros[i] * numeros[i + 1]
            i = 2
        suma_total = suma_total * numeros[i]
        i = i + 1
    print(suma_total)
multiplica_tot(numeros)
