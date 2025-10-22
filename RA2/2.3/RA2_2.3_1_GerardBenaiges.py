# Autor: Gerard Benaiges Murria
# Data: 10/10/2025
# Versió: 1
# Descripció: genera una sequencia de nombres des del 0
# Especificacions de entrada: ficar un numero enter

try:
    num = int(input("Introduix un numero enter "))

    for i in range(0, num):
        print (i)
except ValueError:
    print("Has de ficar un nombre enter")