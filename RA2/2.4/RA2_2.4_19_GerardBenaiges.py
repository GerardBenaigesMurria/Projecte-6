# Autor: Gerard Benaiges Murria
# Data: 05/10/2025
# Versió: 1
# Descripció: Fes una llista de números i multiplica tots els elements per 2
# Especificacions de entrada: ficar cinc nombres enters

numeros = [int(input(f"Introdueix un numero ")) for i in range(5)]

per2 = [n * 2 for n in numeros]

print(per2)