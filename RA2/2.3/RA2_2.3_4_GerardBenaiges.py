# Autor: Gerard Benaiges Murria
# Data: 17/10/2025
# Versió: 1
# Descripció: Et diu tots els numeros parells fins el numero ficat
# Especificacions de entrada: Ficar un numero enter positiu

try:
    num = int(input("Introduix un numero "))

    for i in range(0, num + 1, 2):
        print (i)
except ValueError:
    print("Has de ficar un nombre enter")