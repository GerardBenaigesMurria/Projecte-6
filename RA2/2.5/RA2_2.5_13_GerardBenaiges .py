# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu un mòdul geometria.py amb funcions:area_quadrat(costat),area_cercle(radi), area_rectangle(base, altura)
# Especificacions de entrada: ficar un numero enter

import geometria

costat = int(input("Introdueix el costat del quadrat "))
print("Àrea del quadrat és", geometria.area_quadrat(costat))

radi = int(input("Introdueix el radi del cercle "))
print("Àrea del cercle és", geometria.area_cercle(radi))

base = int(input("Introdueix la base del rectangle "))
altura = int(input("Introdueix l'altura del rectangle "))
print("Àrea del rectangle és", geometria.area_rectangle(base, altura))