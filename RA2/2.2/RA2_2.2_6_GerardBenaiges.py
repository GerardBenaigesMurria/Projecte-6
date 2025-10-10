# Autor: Gerard Benaiges Murria
# Data: 08/10/2025
# Versió: 1
# Descripció: Et diu els 10 primer numeros de fibonacci
# Especificaicons de entrada: 

a,b = 0,1
comptador = 0
while comptador < 10:
    print (a, end=" ")
    suma_termes = a + b
    a = b
    b = suma_termes
    comptador = comptador + 1