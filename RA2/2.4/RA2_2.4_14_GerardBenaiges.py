# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars
# Especificacions de entrada: ficar numeros enters

numeros = [int(input(f"Introdueix el número {i+1}: ")) for i in range(10)]

parells = []
senars = []
for num in numeros:
	if num % 2 == 0:
		parells.append(num)
	else:
		senars.append(num)

print("Nombres introduïts:", numeros)
print("Parells:", parells)
print("Senars:", senars)
