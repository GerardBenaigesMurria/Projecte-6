# Autor: Gerard Benaiges Murria
# Data: 08/10/2025
# Versió: 1
# Descripció: Et diu si el numero que has introduit es primer o no
# Especificaicons de entrada: Introduir un numero enter 

num = int(input("Introdueix un numero "))
num_dividit = 1
resultat = 0
primer = 0
noprimer = 0

while num != num_dividit:
    num_dividit = num_dividit + 1
    resultat = num % num_dividit
    if resultat != 0 and primer >= 1:
        noprimer = noprimer + 1
    if noprimer > 0:
        print("no es primer")
        num_dividit = num
    if resultat == 0 and primer <= 2:
        primer = primer + 1
    if primer < 1:
        print("és primer")
        num_dividit = num
    if num == 2:
        print("és primer")