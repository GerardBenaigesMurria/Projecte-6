# Autor: Gerard Benaiges Murria
# Data: 08/10/2025
# Versió: 1
# Descripció: Has d'endevinar un numero aleatori del 1 al 100
# Especificaicons de entrada: Ficar un numero enter del 1 al 100

import random

adivinar = random.randint(1,100)

numero = 0

while adivinar != numero:
    numero = int(input("Introdueix un numero per endevinar el que penso "))
    
    if numero < adivinar:
        print("El numero és més petit")
    
    if numero > adivinar:
        print("El numero és més gran")
#    print(adivinar)

print("L'has endevinat")    