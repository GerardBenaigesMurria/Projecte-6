# Autor: Gerard Benaiges Murria
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea un mòdul conversions.py amb funcions:celsius_a_fahrenheit(c),fahrenheit_a_celsius(f)
# Especificacions de entrada: ficar un numero enter

import conversions

temp = float(input("Fica una temperatura en Celsius "))

resultat = conversions.celsius_a_fahrenheit(temp)
print(resultat)

temp2 = float(input("Fica una temperatura en Fahrenheit "))

resultat2 = conversions.fahrenheit_a_celsius(temp2)
print(resultat2)