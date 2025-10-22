# Autor: Gerard Benaiges Murria
# Data: 17/10/2025
# Versió: 1
# Descripció: ficar la taula de multiplicacions del numero del usuari
# Especificacions de entrada: ficar un numero enter

try:
    num = int(input("Introduix un numero "))

    for i in range(1, 11):
        print(i, "*", num, "=", i*num)
except ValueError:
    print("Has de ficar un nombre enter")