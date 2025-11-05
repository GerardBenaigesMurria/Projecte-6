# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: Fes un programa que elimini els duplicats d'una llista
# Especificacions de entrada: ficar cadenes de caracters

paraula = [str(input("Introdueix una paraula ")),
           str(input("Introdueix una paraula ")),
           str(input("Introdueix una paraula ")),
           str(input("Introdueix una paraula ")),
           str(input("Introdueix una paraula "))]

paraula_sense_duplicar = list(set(paraula))

print(paraula_sense_duplicar)