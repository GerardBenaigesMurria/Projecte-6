# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal
# Especificacions de entrada: ficar cadenes de caracters

paraules = [str(input("Introdueix una paraula ")) for i in range(5)]

llista_vocal = []

for paraula in paraules:
    if paraula [0].lower() in "aeiou":
        llista_vocal.append(paraula)

print("Paraules que comencen per vocal", llista_vocal)