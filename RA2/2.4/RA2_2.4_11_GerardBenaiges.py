# Autor: Gerard Benaiges Murria
# Data: 31/10/2025
# Versió: 1
# Descripció: Crea una llista amb 5 nombres i imprimeix el major i el menor.
# Especificacions de entrada: ficar numeros enters


nombres = [int(input("Introdueix el primer numero ")),
           int(input("Introdueix el segon numero ")),
           int(input("Introdueix el tercer numero ")),
           int(input("Introdueix el quart numero ")),
           int(input("Introdueix el cinque numero "))]

major = max(nombres)
menor = min(nombres)

print(f"El menor és {menor} i el major és {major}")