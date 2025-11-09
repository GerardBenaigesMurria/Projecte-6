# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Calculadora científica Crea un mòdul cientifica.py que combini funcions del teu mòdul calculadora.py amb funcions del mòdul math (com sqrt, pow, sin, etc.) Mostra un menú on l’usuari triï quin càlcul fer.
# Especificacions de entrada: 

import cientifica
import math
import calculadora

cientifica.mostrar_menu()
comanda = str(input("Introdueix la comanda: "))

if comanda == "1":
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))
    resultat = calculadora.suma(num1, num2)
    print(f"El resultat de la suma és: {resultat}")

if comanda == "2":
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))
    resultat = calculadora.resta(num1, num2)
    print(f"El resultat de la resta és: {resultat}")

if comanda == "3":
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))
    resultat = calculadora.multiplicacio(num1, num2)
    print(f"El resultat de la multiplicació és: {resultat}")

if comanda == "4":
    num1 = float(input("Introdueix el primer número: "))
    num2 = float(input("Introdueix el segon número: "))
    resultat = calculadora.divisio(num1, num2)
    print(f"El resultat de la divisió és: {resultat}")

if comanda == "5":
    num1 = float(input("Introdueix la base: "))
    num2 = float(input("Introdueix l'exponent: "))
    resultat = cientifica.potencia(num1, num2)
    print(f"El resultat de la potència és: {resultat}")

if comanda == "6":
    num = float(input("Introdueix un número: "))
    resultat = math.sqrt(num)
    print(f"L'arrel quadrada de {num} és: {resultat}")

if comanda == "7":
    angle = float(input("Introdueix un angle en graus: "))
    resultat = math.sin(math.radians(angle))
    print(f"El seno de {angle} graus és: {resultat}")

if comanda == "8":
    angle = float(input("Introdueix un angle en graus: "))
    resultat = math.cos(math.radians(angle))
    print(f"El coseno de {angle} graus és: {resultat}")

if comanda == "9":
    angle = float(input("Introdueix un angle en graus: "))
    resultat = math.tan(math.radians(angle))
    print(f"La tangent de {angle} graus és: {resultat}")