# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma
# Especificacions de entrada: ficar un numero enter

num = int(input("Introdueix un numero "))

def factorial(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    print(f"El factorial de {n} és {resultat}")

factorial(num)
