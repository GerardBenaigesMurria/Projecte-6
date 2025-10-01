# Autor: Gerard Benaiges Murria
# Data: 01/10/2025
# Versió: 1
# Descripció: Et diu si has aprovat o has suspes depenen de la teva nota
# Especificaicons de entrada: Introduir un numero del 1 al 10

nota = int(input("Introdueix un numero del 1 al 10 "))

if nota >= 5:
    print("Has aprovat")

if nota < 5:
    print("Has suspes")