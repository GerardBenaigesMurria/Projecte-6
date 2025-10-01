# Autor: Gerard Benaiges Murria
# Data: 01/10/2025
# Versió: 1
# Descripció: Et diu quin numero dels 3 que has ficat es el més gran
# Especificaicons de entrada: Introduir tres numeros enters

num1= int(input("Introdueix el primer numero "))
num2= int(input("Introdueix el segon numero "))
num3= int(input("Introdueix el tercer numero "))

if num1 > num2 and num1 > num3 :
    print(num1)

if num2 > num1 and num2 > num3 :
    print(num2)

if num3 > num1 and num3 > num2 :
    print(num3)