# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: Escriu una funció que retorni la llista al revés (sense reverse())
# Especificacions de entrada: ficar cadenes de caracters

paraules = [str(input("Introdueix una paraula ")) for i in range(5)]

llista = paraules[::-1]

print (llista)